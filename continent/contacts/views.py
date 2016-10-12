from generic.mixins import CategoryListMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import FormView
from contacts.forms import ContactForm

class ContactFormView(FormView, CategoryListMixin):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        sender = form.cleaned_data['sender']
        message = form.cleaned_data['message']
        recipients = ['iamdanteonline@gmail.com']
        message+='\n from: ' + sender
        try:
            send_mail(subject, message, 'iamdanteonline@gmail.com',recipients)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return render(self.request, 'thanks.html')

    def make_breadcrumbs(self):
        result = super(ContactFormView, self).make_breadcrumbs()
        result.append({'empty':'Контакты'})
        return result