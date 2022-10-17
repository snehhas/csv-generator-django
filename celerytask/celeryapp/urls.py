from django.urls import path
from .views import *

urlpatterns=[
    #path('',home,name='homepage'),
    path('success',success,name='successpage'),
    path('savedfiles',finaldata,name='finaldata'),
    path('',newfile,name='newfile'),
]