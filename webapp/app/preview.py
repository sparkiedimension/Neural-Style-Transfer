from django.core.files import File
from PIL import Image
from resizeimage import resizeimage
from webapp.settings import MEDIA_ROOT

def generate_preview( f ):
    file_url = str(f)
    
    fd_img = File(open(MEDIA_ROOT + '/' + file_url, 'r+b'))
    img = Image.open(fd_img)
    
    w, h = img.size;
    ratio = w / h
    
    img = resizeimage.resize_contain(img, [300, int(300 / ratio)])
    img.save(MEDIA_ROOT + '/preview/' + file_url, 'png')
    fd_img.close()
    
    return 'preview/' + file_url
    
