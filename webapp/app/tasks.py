from django.core.serializers import deserialize
from celery import shared_task
from . import models
from . import preview
import time


@shared_task
def apply_img_operations(title, json_obj):
    py_obj = deserialize('json', json_obj)
    
    obj_list = []
    
    i = 0
    
    for obj in py_obj:
        if i <= 1:
            obj.object.preview = preview.generate_preview( obj.object.picture )
            obj.object.save()
        
        obj_list.append(obj.object)
        
        i += 1
        
        
    result_img = stylize( str(obj_list[0]), str(obj_list[1]) )
    result_media = models.Media_Model(picture=result_img, media_type='R', user=obj_list[3])
    result_media.save()
    
    result_media.preview = preview.generate_preview( result_media.picture )
    result_media.save()

    result = models.Result_Model(title=title, content=obj_list[0], style=obj_list[1], result=result_media, user=obj_list[3])
    result.save()
    
    obj_list[2].result = result_media
    obj_list[2].save()

    return "Done " + str(obj_list[2].token)


def stylize( content_name, style_name ):
    time.sleep(10)
    return 'Web-development.jpg'
