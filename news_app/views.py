from django.shortcuts import render
from news_app.models import News,Categories
from django.utils import timezone


# Create your views here.

def project_news_index(request):
    category = Categories.objects.all()
    news = News.objects.all()
    now = timezone.localdate()
    context = {
        "news": news,
        'category':category,
        'now':now,
    }
    return render(request, 'index_1.html', context)


def project_news_detail(request, pk):
    project = News.objects.get(pk=pk)
    category = Categories.objects.all()
    context = {
        'project': project,
        'category':category
    }
    return render(request, 'art.html', context)


