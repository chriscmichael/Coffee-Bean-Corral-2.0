from django.shortcuts import render
from cups.models import Cup
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



class CupListView(ListView):
    model = Cup
    template_name = "cups/list.html"
    context_object_name = "cups_list"


class CupDetailView(DetailView):
    model = Cup
    template_name = "cups/detail.html"


class CupCreateView(CreateView):
    model = Cup
    template_name = "cups/create.html"
    fields = ["date_consumed", "roast_date", "country", "processing_method", "preperation_method","notes", "rating"]
    success_url = reverse_lazy("list_cups")
