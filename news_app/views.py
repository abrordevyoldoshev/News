from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView

from .models import News, Category
from .forms import ContactForms,PostCreateForm


# Create your views here.
def news_list(request):
    # public qilingan malumotlarni 2 hil yol bilan get qilish
    news_lists = News.objects.all().filter(status=News.Status.Published)
    # news_lists = News.published.all()
    # news_lists = News.objects.all()
    context = {
        "news_list": news_lists
    }
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {
        "news": news
    }
    return render(request, 'news/news_detail.html', context=context)


def homePageView(request):
    news_list = News.objects.all().filter(status=News.Status.Published).order_by("-publish_time")[:10]
    local_news = News.published.all().filter(category__name='Mahalliy')[:4]
    category = Category.objects.all()

    context = {
        "news_list": news_list,
        "category": category,
        'local_news': local_news
    }

    return render(request, 'news/home.html', context=context)


# class HomePageView(ListView):
#     model = News
#     template_name = 'news/home.html'
#     context_object_name = 'news'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = self.model.objects.all()
#         context['news_list'] = News.objects.all().filter(status=News.Status.Published).order_by("-publish_time")[:10]
#         context['local_news'] = News.published.all().filter(category__name='Mahalliy')[:4]


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForms
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForms(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h3>Biz bilan aloqaga chiqganinggiz uchun rahmat!")

        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context=context)


def contactPageView(request):
    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h3>Biz bilan aloqaga chiqganinggiz uchun rahmat!")
    context = {
        "form": form
    }

    return render(request, 'news/contact.html', context=context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/foreign.html'
    context_object_name = 'Foreign_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Horij')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news


class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Tehnalogiya')
        return news


class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')


class NewsCreateView(CreateView):
    # form = PostCreateForm
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')

