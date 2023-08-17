from datatime import  views
from django.urls import  path



app_name = 'datatime'


urlpatterns = [
    path('datatime', views.datatime),
    path('', views.hw8_5),
    path('programersday', views.programmersday),
    path('table', views.table),
    # path('password', views.password, name='password' )

]