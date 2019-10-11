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

    preview = models.ImageField(upload_to = 'preview/')
    picture = models.ImageField()
    model_type = models.CharField(max_length = 1, choices = MEDIA_TYPE_CHOICE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __init__(self):
        pass

class Result_Model( models.Model ):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    content = models.ForeignKey(Media_Model, related_name='content_media', on_delete = models.CASCADE)
    result = models.ForeignKey(Media_Model, related_name='result_media', on_delete= models.CASCADE)
    style = models.ForeignKey(Media_Model, related_name='style_media', on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __init__(self):
        pass

    def __str__(self):
        return self.title