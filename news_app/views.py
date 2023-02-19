from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import News, Category
from .forms import ContactForms


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

# def contactPageView(request):
#     form = ContactForms(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h3>Biz bilan aloqaga chiqganinggiz uchun rahmat!")
#     context = {
#         "form": form
#     }
#
#     return render(request, 'news/contact.html', context=context)
