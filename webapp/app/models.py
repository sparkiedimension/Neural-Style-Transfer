from django.db import models
from django.conf import settings

class Media_Model( models.Model ):
    STYLE = 'S'
    CONTENT = 'C'
    MODEL = 'M'
    RESULT = 'R'

    MEDIA_TYPE_CHOICE = [
        (STYLE, 'Style'),
        (CONTENT, 'Content'),
        (MODEL, 'Model'),
        (RESULT, 'Result')
    ]

    preview = models.ImageField(upload_to = 'preview/', null=True)
    picture = models.ImageField()
    media_type = models.CharField(max_length = 1, choices = MEDIA_TYPE_CHOICE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


class Result_Model( models.Model ):
    title = models.CharField(max_length=200)
    content = models.ForeignKey(Media_Model, related_name='content_media', on_delete = models.CASCADE)
    result = models.ForeignKey(Media_Model, related_name='result_media', on_delete= models.CASCADE)
    style = models.ForeignKey(Media_Model, related_name='style_media', on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    

class Token_Model( models.Model ):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    token = models.CharField(max_length=32, null=False)
    result = models.ForeignKey(Media_Model, related_name='token_result_media', on_delete= models.CASCADE, null=True)
    
    
