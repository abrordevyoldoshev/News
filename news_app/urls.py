from django.urls import path
from .views import news_list, news_detail, homePageView,ContactPageView
urlpatterns = [
    path('', homePageView, name='home_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path("news_all/", news_list, name='all_news_list'),
    path("<slug:news>/", news_detail, name="news_detail")
]