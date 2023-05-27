from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogModel
from django.urls import reverse_lazy

# Create your views here.
# 一覧画面
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# 詳細画面
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

# 作成画面
class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category') # 表示させるフィールド
    success_url = reverse_lazy('list') # 送信時のurlを指定

# 削除画面
class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

# 更新画面
class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')