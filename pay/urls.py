from django.urls import path
from .views import home, success

urlpatterns = [
    path('', home, name='home'),
    path('sucess/', success , name='sucess')
    
]