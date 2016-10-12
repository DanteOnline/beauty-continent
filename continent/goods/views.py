from django.http import HttpResponse
from django.views.generic.list import ListView
from generic.mixins import CategoryListMixin
from goods.models import Good
from categories.models import Subcategory
from django.views.generic.detail import DetailView
from django_comments.models import Comment
from django.views.generic.base import ContextMixin


class GoodsListView(ListView,  CategoryListMixin):
    model = Good
    template_name = 'goods_index.html'
    paginate_by = 9
    cat = None
    view = None
    count = 10

    def make_breadcrumbs(self):
        result = super(GoodsListView, self).make_breadcrumbs()
        result.append({'empty':self.cat.name})
        return result

    def get(self, request, *args, **kwargs):
        try:
            self.view = self.request.session['view']
        except:
            self.view = 'grid3'

        if self.view != 'list':
            count = self.view.replace('grid','')
            self.count = int(count)
            if self.count == 3:
                self.paginate_by = 9
            elif self.count == 4:
                self.paginate_by = 12
            else:
                self.paginate_by = 6
        else:
            self.paginate_by = 5

        if self.kwargs['pk'] == None:
            self.cat = Subcategory.objects.first()
        else:
            self.cat = Subcategory.objects.get(pk=self.kwargs['pk'])
        return super(GoodsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        #количество товаров в строке
        context['good_count'] = self.count
        return context

    def get_queryset(self):
        goods = Good.objects.filter(category=self.cat)
        # сортировка
        # 1 - price
        # 0 - name
        '''
        if self.sort == '1':
            if self.order == 'D':
                goods = goods.order_by('-price', 'name')
            else:
                goods = goods.order_by('price', 'name')
        else:
            if self.order == 'D':
                goods = goods.order_by('-name')
            else:
                goods = goods.order_by('name')
        '''
        return goods

class GoodDetailView(DetailView, CategoryListMixin):
    model = Good
    template_name = 'good.html'
    count = None

    def make_breadcrumbs(self):
        result = super(GoodDetailView, self).make_breadcrumbs()
        result.append({self.good.category.get_absolute_url(): self.good.category.name})
        result.append({'empty':self.good.name})
        return result

    def get(self, request, *args, **kwargs):
        good_pk = self.kwargs['pk']
        self.good = Good.objects.get(pk=good_pk)
        return super(GoodDetailView, self).get(request, *args, **kwargs)


def change_view(request):
    if request.method == "GET":
        request.session['view'] = request.GET['view']
        return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')