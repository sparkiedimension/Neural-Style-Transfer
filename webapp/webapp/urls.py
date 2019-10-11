from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, static
from . import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view()),
    path('app/', include('app.urls'))
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'webapp.views.ErrorPageView'
