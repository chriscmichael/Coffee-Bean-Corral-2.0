from django.shortcuts import render
from beans.models import Bean
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



class BeanListView(ListView):
    model = Bean
    template_name = "beans/list.html"
    context_object_name = "beans_list"


class BeanDetailView(DetailView):
    model = Bean
    template_name = "beans/detail.html"


class BeanCreateView(CreateView):
    model = Bean
    template_name = "beans/create.html"
    fields = ["order_number", "purchase_date", "country", "varietal", "process", "growing_region", "washing_station","elevation","notes"]
    success_url = reverse_lazy("list_beans")
