from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Culture, Disease, Drug


def home_view(request):
    context = {
        'total_cultures': Culture.objects.count(),
        'total_diseases': Disease.objects.count(),
        'total_drugs': Drug.objects.count(),
    }
    return render(request, 'agro_catalog/home.html', context)


class CultureListView(ListView):
    model = Culture
    template_name = 'agro_catalog/culture_list.html'
    context_object_name = 'cultures'


class DiseaseListView(ListView):
    model = Disease
    template_name = 'agro_catalog/disease_list.html'
    context_object_name = 'diseases'


class DrugListView(ListView):
    model = Drug
    template_name = 'agro_catalog/drug_list.html'
    context_object_name = 'drugs'


class CultureDetailView(DetailView):
    model = Culture
    template_name = 'agro_catalog/culture_detail.html'
    context_object_name = 'culture'


class DiseaseDetailView(DetailView):
    model = Disease

    def get_queryset(self):
        return Disease.objects.prefetch_related('cultures', 'drugs')

    template_name = 'agro_catalog/disease_detail.html'
    context_object_name = 'disease'


class DrugDetailView(DetailView):
    model = Drug

    def get_queryset(self):
        return Drug.objects.prefetch_related('fights_diseases')

    template_name = 'agro_catalog/drug_detail.html'
    context_object_name = 'drug'
