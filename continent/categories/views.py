from django.shortcuts import render
from categories.models import Subcategory
from django.views.generic.list import ListView

# Create your views here.
class SubcategoriesView(ListView):
    model = Subcategory
    paginate_by = 9
