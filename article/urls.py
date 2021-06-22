
from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register("article/search", views.ArticleSearchView, basename='article-search')
router.register('article', views.ArticleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

]
