from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from core.models import Item


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class ItemListView(ListView):
    model = Item
    template_name = "items_list.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"
