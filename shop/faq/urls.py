from django.conf.urls import url
from faq.views import FaqListView

urlpatterns = [
    url(r'^$', FaqListView.as_view(), name = 'faq')
]