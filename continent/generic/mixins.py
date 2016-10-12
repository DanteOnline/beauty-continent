from django.views.generic.base import ContextMixin
from categories.models import Category, Subcategory
from django.core.urlresolvers import reverse

class CategoryListMixin(ContextMixin):
    '''def get_url_parts(self):
        current_url = self.current_url
        all_parts = current_url.split('/')
        parts = []
        for part in all_parts:
            if part:
                parts.append(part)
        return parts'''

    def make_breadcrumbs(self):
        url = reverse('main')
        return [{url:'Главная страница'}]

    current_url = None
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        self.current_url = self.request.path
        #context['current_url'] = self.current_url
        context['breadcrumbs'] = self.make_breadcrumbs()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context