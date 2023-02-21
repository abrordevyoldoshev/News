from news_app.models import News


def latest_news(request):
    latest_newses = News.published.all().order_by("-publish_time")[:10]

    context = {
        'latest_newses': latest_newses
    }
    return context
