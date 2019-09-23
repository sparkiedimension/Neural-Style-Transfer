from django.http import HttpResponse, HttpResponseNotFound

def HomeView( request ):
    return HttpResponse( "Yeah, this is homepage!" )

def ErrorPageView( request, exception ):
    return HttpResponseNotFound( "What? There is nothing here!" )