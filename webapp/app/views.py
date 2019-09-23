#from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class ImageUploadView( View ):
    def __init__( self ):
        pass

    def get( self, request ):
        return HttpResponse( "Hi from App!" )