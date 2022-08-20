from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from .models import Article, Category
# Create your views here.
class TopView(TemplateView):
    template_name = 'top.html'

class IndexView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.order_by('-date')

class ArticleDetail(DetailView):
    model = Article
    template_name = 'detail.html'

class CategoryView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        #category = get_object_or_404(Category, pk = self.kwargs['pk'])
        category = Category.objects.get(name = self.kwargs['category'])
        queryset = Article.objects.order_by('-date').filter(category = category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['category'] = get_object_or_404(Category, pk = self.kwargs['pk'])
        context['category'] = self.kwargs['category']
        return context

