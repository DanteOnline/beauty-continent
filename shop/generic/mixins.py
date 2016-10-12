from django.views.generic.base import ContextMixin
from items.models import Item
from django.core.urlresolvers import reverse

class TopListMixin(ContextMixin):

    def make_breadcrumbs(self):
        url = reverse('main')
        return [{url:'Главная страница'}]

    def get_context_data(self, **kwargs):
        context = super(TopListMixin, self).get_context_data(**kwargs)
        context['tops'] = Item.get_tops()
        context['breadcrumbs'] = self.make_breadcrumbs()
        return context