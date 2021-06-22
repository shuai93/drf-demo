from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from .search_indexes import ArticleIndex
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleHaystackSerializer(HaystackSerializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        index_classes = [ArticleIndex]

        fields = ['title', 'creator', 'content', 'tag']
