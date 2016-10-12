from generic.mixins import CategoryListMixin
from faq.models import Faq
from django.views.generic.list import ListView
# Create your views here.
class FaqListView(ListView, CategoryListMixin):
    model = Faq
    template_name = 'faq.html'
    paginate_by = 100

    def make_breadcrumbs(self):
        result = super(FaqListView, self).make_breadcrumbs()
        result.append({'empty':'Часто задаваемые вопросы'})
        return result