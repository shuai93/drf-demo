import logging

from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer, ArticleHaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from utils.base_mixin import ExceptionMixin


logger = logging.getLogger('demo')


class ArticleSearchView(HaystackViewSet):

    index_models = [Article]

    serializer_class = ArticleHaystackSerializer


class ArticleViewSet(viewsets.ModelViewSet, ExceptionMixin):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


