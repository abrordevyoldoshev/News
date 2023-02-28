from django.urls import path

from .views import news_list, news_detail, homePageView, ContactPageView, LocalNewsView, ForeignNewsView, \
    TechnologyNewsView, SportNewsView, NewsDeleteView, NewsUpdateView, NewsCreateView

urlpatterns = [
    path('', homePageView, name='home_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path("technology/", TechnologyNewsView.as_view(), name='technology_news_page'),
    path("create/", NewsCreateView.as_view(), name='news_create'),
    path("<slug:news>/", news_detail, name='news_detail'),
    path("<slug>/delete/", NewsDeleteView.as_view(), name='news_delete'),
    path("<slug>/edit>/", NewsUpdateView.as_view(), name='news_update'),
    path("news_all/", news_list, name='all_news_list'),
]
