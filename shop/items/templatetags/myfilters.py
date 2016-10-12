from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='addplaceholder')
def addplaceholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})

@register.filter(name='to_bs')
def to_bs(value, arg):
    return value.as_widget(attrs={'class': 'form-control', 'placeholder': arg})