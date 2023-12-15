from django.contrib import admin
from django.urls import path
from .views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about ,name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery ,name='gallery'),
    path('index/', index, name='index'),
    path('services/', services, name='services'),
    
    path('login/' ,  log_in , name='login/' ),
    path('signup/' , sign_up , name = 'signup/') ,
    path('logout/' , log_out , name = 'logout') 
 
  
]

