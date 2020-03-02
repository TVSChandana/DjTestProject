from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_items),
    path('data/', views.myView),
]
