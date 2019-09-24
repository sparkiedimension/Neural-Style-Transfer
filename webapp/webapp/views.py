from django.shortcuts import render

def HomeView( request ):
    context_dict = {
        'title': "NST Homepage",
        'content': "Yeah Baby, this is the homepage"
    }
    return render( request, 'homepage.html', context_dict )

def ErrorPageView( request, exception ):
    context_dict = {
        'title': "Error 404 | NST",
        'content': "Umm, something went wrong. Are you sure this is the page you're looking for?"
    }
    return render( request, 'error_404.html', context_dict )