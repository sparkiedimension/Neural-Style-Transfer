from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
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
        self.update_context( request )
        self.context_dict['title'] = 'Dashboard | NST'
        
        final_dict = self.context_dict
        
        return render( request, 'dashboard.html', final_dict )
