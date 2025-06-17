from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

from datetime import datetime

# Create your views here.

def index(request):
    article_records = Post.objects.all()
    article_list = list()
    for count, article in enumerate(article_records):
        article_list.append("#{}: {}<br>" . format(str(count), str(article.title)))
        article_list.append("<small>{}</small><br>" . format(article.content))
        article_list.append("slug: {}<br><hr>" . format(article.slug))

    return HttpResponse(article_list)

def about(request):
    return HttpResponse('hello world')

def index_use_template(request):
    article_records = Post.objects.all()
    now = datetime.now()
    # return render(request, "index.html", locals()) # {'now': now}
    return render(request, "pages/home.html",locals())

def showPost(request, slug):
    article = Post.objects.get(slug = slug)
    return render(request, "pages/post.html", locals())

def login(request):
    return render(request, 'pages/login.html')