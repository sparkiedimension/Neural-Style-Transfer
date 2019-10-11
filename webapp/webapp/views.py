from django.shortcuts import render
from app import views

class HomeView( views.NavbarView ):
    def __init__( self ):
        super().__init__()

    def get( self, request ):
        self.update_context( request )
        self.context_dict['title'] = 'NST Homepage'
        return render( request, 'homepage.html', self.context_dict )

def ErrorPageView( request, exception ):
    context_dict = {
        'title': "Error 404 | NST",
        'content': "Umm, something went wrong. Are you sure this is the page you're looking for?"
    }
    return render( request, 'error_404.html', context_dict )