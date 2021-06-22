from .models import Article
from haystack import indexes


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    content = indexes.CharField(model_attr="content")
    tag = indexes.CharField(model_attr="tag")
    creator = indexes.CharField(model_attr="creator")
    id = indexes.CharField(model_attr="pk")
    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.title,
        ))

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
