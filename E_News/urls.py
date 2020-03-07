from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_items),
    path('data/', views.myView),
    path('crimeNews/', views.crimeNewsDisplay),
    path('economicNews/', views.economicNewsDisplay),
    path('politicNews/', views.politicNewsDisplay),
    path('sportsNews/', views.sportNewsDisplay),
    path('foreignNews/', views.foreignNewsDisplay),
]
