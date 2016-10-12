from faq.models import Faq
from django.views.generic.list import ListView
from generic.mixins import TopListMixin
# Create your views here.
class FaqListView(ListView, TopListMixin):
    model = Faq
    template_name = 'faq.html'
    paginate_by = 100

    def make_breadcrumbs(self):
        result = super(FaqListView, self).make_breadcrumbs()
        result.append({'empty':'Часто задаваемые вопросы'})
        return result