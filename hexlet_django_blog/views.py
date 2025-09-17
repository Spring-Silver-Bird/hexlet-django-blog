# hexlet_django_blog/views.py
from django.shortcuts import render
from django.views.generic.base import TemplateView


'''def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World",
        },
    )'''


'''def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )'''


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "bunch of bloody loonies"
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        tags = ["обучение", "программирование", "python", "oop"]
        context = super().get_context_data(**kwargs)
        context["tags"] = tags
        return context


'''class ArticleCommentsView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(
            Comment, id=kwargs["id"], article__id=kwargs["article_id"]
        )

        return render(...)'''