from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from django.forms.models import model_to_dict
# Create your views here.
from json import dumps

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view'

def news_home(request):
    # news = Articles.objects.all()
    data = list(Articles.objects.values())
    return JsonResponse({'data': data})

def news_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    return JsonResponse({ 'data': model_to_dict(article) })
