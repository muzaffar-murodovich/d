from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

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
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:15]
    local_news = News.published.all().filter(category__title="Mahalliy").order_by("-publish_time")[:5]

    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
    }
    return render(request, 'news/home.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:15]
        return context

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us.")

        return render(request, 'news/contact.html', {'form': form})


def categoryPageView(request):
    context = {}
    return render(request, 'news/category.html', context)

def singlePageView(request):
    context = {}
    return render(request, 'news/single.html', context)

def basePageView(request):
    context = {}
    return render(request, 'news/base.html', context)