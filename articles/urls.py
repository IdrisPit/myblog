from django.urls import path
from . import views


urlpatterns = [
    path("", views.ArticleView.as_view(), name="home"),
    path("articles/<int:pk>", views.ArticleDetailView.as_view(), name="article_page")
]
