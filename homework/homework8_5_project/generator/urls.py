from generator import  views
from django.urls import  path



app_name = 'generator'


urlpatterns = [
    path('', views.home),
    path('password', views.password, name='password' )

]
