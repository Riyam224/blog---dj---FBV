from django.shortcuts import render
from .models import Article
# Create your views here.
from .forms import ArticleForm


def article_list(request):

    myArticle = Article.objects.all()
    context = {
        'article_list': myArticle
    }
    return render(request, 'blog/article_list.html', context)


def article_details(request):
    if request.method == 'POST':
        form = ArticleForm(request.Post)
        if form.is_valid():
            form.save()
    form = ArticleForm()
    context = {
        'form': form
    }

    return render(request, 'blog/article_details.html', context)
