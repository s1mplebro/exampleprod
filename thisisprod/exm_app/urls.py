from django.urls import path
from .views import HomePageView,PageView

urlpatterns = [
path('',HomePageView.as_view(),name='index'),
path('domoy/',PageView.as_view(),name='home'),

#path('',HomePageView.as_view(),name='base')
]