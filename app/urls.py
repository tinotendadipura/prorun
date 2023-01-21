from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.home, name='home'),
    path('About-Us', views.about_us, name='About-Us'),
    path('get-Quote', views.get_quote, name='get-Quote'),
    path('services', views.services, name='services'),
    path('our-work', views.our_work, name='our-work'),
    path('shop', views.shop, name='shop'),

    path('contact-us', views.contact_us, name='contact-us'),
    
]