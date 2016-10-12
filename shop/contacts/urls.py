from django.conf.urls import url
from contacts.views import  ContactFormView

urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name = 'contacts'),
]