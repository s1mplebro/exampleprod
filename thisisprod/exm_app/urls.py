from django.urls import path
from .views import HomePageView,PageView,aPageViewAbout

urlpatterns = [
path('',HomePageView.as_view(),name='index'),
path('domoy/',PageView.as_view(),name='home'),
path('aboutus/',aPageViewAbout.as_view(),name='about'),
]