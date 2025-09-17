from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]


'''class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]'''