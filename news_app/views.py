from django.shortcuts import render, get_object_or_404
from .models import News, Category


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


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)

    context = {
        "news": news
    }
    return render(request, 'news/news_detail.html', context=context)


def homePageView(request):
    news = News.objects.all().filter(status=News.Status.Published)
    category = Category.objects.all()

    context = {
        "news": news,
        "category": category,
    }

    return render(request, 'news/home.html', context=context)


def contactPageView(request):
    context = {

    }

    return render(request, 'news/contact.html', context=context)
