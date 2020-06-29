from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Product, Category
from .forms import ProductForm
from .utils import MyMixin

class HomeProduct(MyMixin, ListView):
    model = Product
    template_name = 'product/home_product_list.html'
    context_object_name = 'product'
    # extra_context = {'title': 'Главная'}
    # mixin_prop = 'hello world'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('category')


class ProductByCategory(MyMixin, ListView):
    model = Product
    template_name = 'product/home_product_list.html'
    context_object_name = 'product'
#    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewProduct(DetailView):
    model = Product
    context_object_name = 'product_item'

class CreateProduct(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'product/add_product.html'
    # success_url = reverse_lazy('home')
    #login_url = '/admin/'
    raise_exception = True
