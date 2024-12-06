from django.urls import path
from taskapp.views import *
urlpatterns = [
    path('',home,name='home'),
    path('main/',Task.as_view(),name='main'),
    path('create/',NewTask.as_view(),name='create'),
    path('update/<int:pk>',TaskUpdate,name='update'),
    path('delete/<int:pk>',delete,name='delete'),

   
    
]
