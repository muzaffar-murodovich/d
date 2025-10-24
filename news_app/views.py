from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm
# Create your views here.


def news_list(request):
    news_list = News.published.all()

    context = {
        'news_list': news_list,
    }

    return render(request, 'news/news_list.html', context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news": news,
    }
    return render(request, 'news/news_detail.html', context)

def homePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'news/home.html', context)

def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2> Biz bilan bogʻlanganingiz uchun rahmat </h2>")
    context = {
        'form': form
    }
    return render(request, 'news/contact.html', context)

def categoryPageView(request):
    context = {}
    return render(request, 'news/category.html', context)

def singlePageView(request):
    context = {}
    return render(request, 'news/single.html', context)

def basePageView(request):
    context = {}
    return render(request, 'news/base.html', context)