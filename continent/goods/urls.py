from django.conf.urls import url
from goods.views import GoodsListView, GoodDetailView, change_view

urlpatterns = [
    url(r'(?P<pk>\d+)/$', GoodsListView.as_view(), name='goods'),
    url(r'(?P<pk>\d+)/detail/$', GoodDetailView.as_view(), name='goods_detail'),
    url(r'change_view/$', change_view, name='change_view'),
]