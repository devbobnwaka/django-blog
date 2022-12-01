from django.urls import path
from . import views 

app_name='clients'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('news/', views.news, name='news'),
]


