from generic.mixins import TopListMixin
from items.models import Item
from django.views.generic.detail import DetailView
from django.http import HttpResponse

# Create your views here.
class ItemDetailView(DetailView, TopListMixin):
    model = Item
    view = None

    def set_view_default(self):
        # устанавливаем значении сессии по умолчанию на сетку
        try:
            self.view = self.request.session['view']
        except:
            self.view = 'grid'

    def get(self, request, *args, **kwargs):
        self.set_view_default()
        return super(ItemDetailView, self).get(request, *args, **kwargs)

    def make_breadcrumbs(self):
        result = super(ItemDetailView, self).make_breadcrumbs()
        add_result = []
        parent = self.object
        while parent != None:
            add_result.append({parent.get_url:parent.name})
            parent = parent.parent
        add_result.reverse()
        result.extend(add_result)
        return result

def change_view(request):
    if request.method == "GET":
        request.session['view'] = request.GET['view']
        return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')