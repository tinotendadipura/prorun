from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
     
] + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)


admin.site.site_header ='Portal DataBase'
admin.site.index_title ='E Learning'
admin.site.site_title = 'E learning DB'
