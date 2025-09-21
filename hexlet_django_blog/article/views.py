from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.contrib import messages
from .models import ArticleComment
from hexlet_django_blog.views import IndexView

# Create your views here.
from django.http import HttpResponse


'''def index(request):
    return HttpResponse("article/index.html")'''

'''def index(request, tags, article_id):
    return render(
        request,
        "index.html",
        context={
            'who': 'Article',
        })'''

ARTICLES = [
    {"id": 1, "title": "Первая статья", "tags": "python"},
    {"id": 2, "title": "Вторая статья", "tags": "ооз"},
    {"id": 3, "title": "Третья статья", "tags": "python"},
    {"id": 4, "title": "Четвертая статья", "tags": "blog"},
    {"id": 5, "title": "Пятая статья", "tags": "python"},
    {"id": 6, "title": "Шестая статья", "tags": "python"},
    {"id": 7, "title": "Седьмая статья", "tags": "ооп"},
    {"id": 8, "title": "Восьмая статья", "tags": "python"},
    {"id": 9, "title": "Девятая статья", "tags": "blog"},
    {"id": 10, "title": "Десятая статья", "tags": "python"},
]


class ArticleListView(IndexView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = ARTICLES
        return context

class ArticleDetailView(IndexView):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )


'''class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            comment = form.save(commit=False)  # Получаем заполненную модель
            # Дополнительно обрабатываем модель
            comment.content = check_for_spam(form.data["content"])
            comment.save()'''


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, 'The article has been created successfully.')
            return redirect('article_list')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been updated successfully.')
            return redirect("article_list")
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(
                request, "articles/update.html", {"form": form, "article_id": article_id}
            )

def index(request, tags=None, article_id=None):
    article_id = 42
    tags = 'python'

    # return redirect(reverse('article', kwargs={'article_id': article_id, 'tags': tags}))
    return render(request, 'articles/index.html', context={'article_id': article_id, 'tags': tags})