from django.urls import path
from . import views

app_name = 'administrators'
urlpatterns = [
    path('views/', views.views, name='views'),
    path('create/', views.create, name='create'),
    path('edit/<slug:slug>/', views.edit, name='edit'),
    path('delete/<slug:slug>/', views.delete, name='delete'),
]
