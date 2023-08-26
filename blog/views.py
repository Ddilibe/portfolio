from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import edit, detail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q, F
from django.views import generic
from blog import models as md
from blog import forms as fm
import random
import uuid

# Create your views here.

class LandingPageView(generic.TemplateView):

    template_name = "landing_page.html"

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class BlogCreateView(edit.CreateView):

    form_class = fm.BlogForm
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy("all_blog")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.id = uuid.uuid4()
        return super().form_valid(form)

class TagBlogCreateView(edit.CreateView):

    form_class = fm.TagBlogForm
    template_name = "blog/create_tag.html"
    success_url = reverse_lazy('all_blog_tags')

    def form_valid(self, form):
        form.instance.id = uuid.uuid4()
        values = ['primary', 'secondary', 'success', "danger", "warning"]
        values += ['info', "light", "dark"]
        form.instance.background_color = random.choice(values)
        return super().form_valid(form)

class BlogDetailView(detail.DetailView):

    model = md.Blog
    template_name = "blog/detail_view.html"

    def dispatch(self, request, name, *args, **kwargs):
        if blog := md.Blog.objects.get(id=name):
            blog.views = F("views") + 1
            blog.save(update_fields=['views'])
        return super().dispatch(request, name, *args, **kwargs)

    def get(self, request, name, *args, **kwargs):
        vale, context = md.Blog.objects.get(id=name), {}
        context['values'], context['tags'] = vale, vale.tags.all()[:3]
        context['related'] = md.Blog.objects.filter(
            tags__in=[name for name in vale.tags.all()]
            ).filter(~Q(id=vale.id))[:3]
        return render(request, self.template_name, context)


class TagBlogDetailView(detail.DetailView):

    model = md.TagBlog
    template_name = "blog/tag_detail_view.html"

    def get(self, request, name, *args, **kwargs):
        tag = md.TagBlog.objects.get(id=name)
        blog = md.Blog.objects.filter(tags=name).order_by('views')[:3]
        return render(request, self.template_name, {'tag':tag, 'blogs':blog})


class BlogUpdateView(edit.UpdateView):

    model = md.Blog
    form_class = fm.BlogForm
    template_name = 'blog/blog_update_view.html'
    success_url = reverse_lazy('all_blog')

    def get(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data()['title'] = self.object.title
        return super().get(request, pk, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TagBlogUpdateView(edit.UpdateView):

    form_class = fm.TagBlogForm
    template_name = 'blog/tag_update_view.html'


class TagBlogDeleteView(edit.DeleteView):

    form_class = fm.TagBlogForm
    success_url = "home"


class BlogDeleteView(edit.DeleteView):

    form_class = fm.BlogForm
    success_url = "home"

class BlogLandingView(generic.ListView):

    model = md.Blog
    template_name = 'blog/blogs.html'
    queryset = md.Blog.objects.order_by('views')[:9]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['top'] = md.Blog.objects.all().order_by('-views')[0]
        context['trending'] = md.Blog.objects.all().order_by('-views')[1:4]
        context['latest'] = md.Blog.objects.all().order_by('-update_date')[:3]
        # print([(name.title, name.views) for name in md.Blog.objects.all().order_by('views') ])
        return context


class TagBlogListView(generic.ListView):

    model = md.TagBlog
    template_name = 'blog/blogtags.html'
    context_object_name = "tags"


class BlogShowAllView(generic.ListView):

    model = md.TagBlog
    template_name = 'blog/all_blog.html'
