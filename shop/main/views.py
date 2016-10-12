from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import TopListMixin

class MainPageView(TemplateView, TopListMixin):
    template_name = 'mainpage.html'