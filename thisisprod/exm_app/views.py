from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'index.html'
	

class PageView(TemplateView):
	template_name = 'home.html'

class aPageViewAbout(TemplateView):
	template_name = 'about.html'