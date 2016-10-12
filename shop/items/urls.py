from django.conf.urls import url
from items.views import ItemDetailView, change_view

urlpatterns = [
    url(r'(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
    url(r'change_view/$', change_view, name='change_view'),
]