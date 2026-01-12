from django.shortcuts import render
from unicodedata import category

from .models import News , Category
from django.shortcuts import render, get_object_or_404


def news_list(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all
    context={
        'news':news
    }
    return render(request ,'list.html', context=context)



def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {
        'news': news
    }
    return render(request, 'detail.html', context)

def home_page_view(request):
    categories = Category.objects.all()
    news = News.objects.filter(status = News.Status.Published)
    context = {
        'categories':categories,
        'news':news
    }
    return render(request, 'home.html', context)



def contact_us(request):
    context = {}
    return render(request, 'contact.html' , context)