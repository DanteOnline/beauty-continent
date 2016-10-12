from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
    sender = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class':'form-control'}))