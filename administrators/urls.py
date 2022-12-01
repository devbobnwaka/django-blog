from django.urls import path
from . import views

app_name = 'administrators'
urlpatterns = [
    path('views/', views.views, name='views'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
]
