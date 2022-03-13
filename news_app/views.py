from django.shortcuts import render
from news_app.models import News


# Create your views here.

def project_news_index(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request, 'news.html', context)


def project_news_detail(request, pk):
    project = News.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'news_detail.html', context)