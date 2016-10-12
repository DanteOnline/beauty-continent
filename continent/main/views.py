from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
#from goods.models import Good

class MainPageView(TemplateView, CategoryListMixin):
    template_name = 'mainpage.html'
    #all_goods = Good.objects.all()
    #goods = all_goods.filter(featured=True)

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        #context['news'] = self.news
        #context['goods'] = self.goods
        #context['all_goods'] = self.all_goods
        return context