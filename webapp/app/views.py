from django.shortcuts import render
from django.views import View
# Create your views here.

class ImageUploadView( View ):
    def __init__( self ):
        self.context_dict = {
            'title': "Image Upload | NST",
            'content': "Something about image upload!"
        }

    def get( self, request ):
        return render( request, 'imgupload.html', self.context_dict )