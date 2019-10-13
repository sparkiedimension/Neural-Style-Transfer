from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse
from . import models
from . import tasks
import time
# Create your views here.


def auth_logout( request ):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')



class NavbarView( View ):
    context_dict = {}

    def init_context( self ):
        self.context_dict = {
            'title': "",
            'nav_items': {
                'showcase': {
                    'text': 'showcase',
                    'link': '/showcase/',
                    'child': {}
                }
            }
        }

    def update_context( self, request ):
        self.init_context()

        if request.user.is_authenticated:
            self.context_dict['nav_items'][request.user.username] = {
                'text': request.user.username,
                'link': 'javascript:;',
                'child': {
                    'logout' : {
                        'text': 'LOG OUT',
                        'link': '/app/logout/'
                    }
                }
            }
        else:
            self.context_dict['nav_items']['signin'] = {
                'text': 'Sign In',
                'link': '/app/login/',
                'child': {}    
            }



class LoginView( NavbarView ):
    def __init__( self ):
        super().__init__()

    def get( self, request ):
        if request.user.is_authenticated:
            logout(request)

        self.update_context( request )
        self.context_dict['title'] = 'Login | NST'
        self.context_dict['nav_items']['signin'] = {
            'text': 'Register',
            'link': '/app/register/'
        }

        return render( request, 'login.html', self.context_dict )

    def post( self, request ):
        self.update_context( request )
        self.context_dict['title'] = 'Login | NST'
        self.context_dict['nav_items']['signin'] = {
            'text': 'Register',
            'link': '/app/register/'
        }
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        
        final_dict = self.context_dict
        final_dict.update({ 'has_error': True })

        return render( request, 'login.html', final_dict )



class RegisterView( NavbarView ):
    def __init__( self ):
        super().__init__()

    def get( self, request ):        
        if request.user.is_authenticated:
            logout(request)

        self.update_context( request )
        self.context_dict['title'] = 'Register | NST'

        return render( request, 'register.html', self.context_dict )

    def post( self, request ):
        self.update_context( request )
        self.context_dict['title'] = 'Register | NST'
        
        username = request.POST['username']
        password = request.POST['password']
        email = "someone@example.com"

        user = User.objects.create_user(username, email, password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        
        final_dict = self.context_dict
        final_dict.update({ 'has_error': True })

        return render( request, 'register.html', final_dict )



class DashboardView( LoginRequiredMixin, NavbarView ):
    login_url = '/app/login/'
    
    def __init__( self ):
        pass
    
    def get( self, request ):
        if 'token' in request.GET:
            json = {}
            
            token_entry = get_object_or_404( models.Token_Model, token=request.GET['token'] )
        
            if token_entry is not None:
                if token_entry.result is not None:
                    result_entry = get_object_or_404( models.Result_Model, result=token_entry.result)
                    
                    if result_entry is not None:
                        json = {
                            'token': request.GET['token'],
                            'title': result_entry.title,
                            'final': token_entry.result.preview.url,
                            'content': result_entry.content.preview.url,
                            'style': result_entry.style.preview.url
                        }
            
            return JsonResponse(json)
        
        
        self.update_context( request )
        self.context_dict['title'] = 'Dashboard | NST'
        
        models.Token_Model.objects.filter( user=request.user, result__isnull=False ).delete()
        
        infant_set_query = models.Token_Model.objects.filter( user=request.user )
        ready_set_query = models.Result_Model.objects.filter( user=request.user )
        
        infant_set = []
        ready_set = []
        
        for infant_obj in infant_set_query:
            infant_set.append({ 'token': infant_obj.token })
            
        for ready_obj in ready_set_query:
            ready_set.append({ 
                'title': ready_obj.title,
                'content_url': ready_obj.content.preview.url,
                'style_url': ready_obj.style.preview.url,
                'result_url': ready_obj.result.preview.url,              
            })
        
        infant_set = [entry for entry in infant_set]
        ready_set = [entry for entry in ready_set]
        
        final_dict = self.context_dict
        final_dict.update({
            'infant_set': infant_set,
            'ready_set': ready_set
        })
        
        print(final_dict)
        
        return render( request, 'dashboard.html', final_dict )
    
    
    def post( self, request ):
        title = request.POST['design-title']
        content = request.FILES['content-upload']
        style = request.FILES['style-upload']
        
        content = models.Media_Model(picture=content, media_type='C', user=request.user)
        style = models.Media_Model(picture=style, media_type='S', user=request.user)
        
        content.save()
        style.save()
        
        token_str = self.generate_token()
        
        token = models.Token_Model(user=request.user, token=token_str)
        token.save()
        
        py_obj = [content, style, token, request.user]
        
        json_obj = serialize('json', py_obj)
        
        tasks.apply_img_operations.delay(title, json_obj)
        
        return redirect('/app/dashboard')
    
    
    def generate_token(self):
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        return str(hash(current_time))
