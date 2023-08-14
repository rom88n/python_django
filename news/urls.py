from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home),
    path('<int:pk>', views.news_detail),
]
