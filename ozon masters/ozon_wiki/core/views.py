from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import Count
from django.views import View
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Oblast, Category, Article
# Create your views here.


def main(request):
    oblasts = Oblast.objects.all().annotate()
    categories = Category.objects.all().annotate()

    q = request.GET.get('q')
    if q is not None:   
        oblasts = oblasts.filter(title__icontains=q)


    return render(request, 'core/main.html', context={
        'oblasts': oblasts,
        'categories': categories
    })

def categ_list(request, pk):
    categories = Category.objects.all().annotate()
    try:
        oblasts = Oblast.objects.get(pk=pk)
    except Oblast.DoesNotExist:
        raise Http404
    return render(request, 'core/categ_list.html', context={
        'oblasts': oblasts,
        'categories': categories,
    })

def article_list(request, pk2):
    articles = Article.objects.all().annotate()
    try:
        categories = Category.objects.get(pk=pk2)
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'core/article_list.html', context={
        'articles': articles,
        'categories': categories,
    })

def article(request, pk3):
    articles = Article.objects.all().annotate()
    categories = Category.objects.all().annotate()
    try:
        articles = Article.objects.get(pk=pk3)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'core/article.html', context={
        'articles': articles,
        'categories': categories,
            })

# def topic_details2(request, pk2):
#     try:
#         topic2 = Topic.objects.get(pk=pk2)
#     except Topic.DoesNotExist:
#         raise Http404
#     return render(request, 'core/topic_details2.html', context={
#         'topic2': topic2
#     })

# def teacher_list(request):
#     teachers = Teacher.objects.all().annotate()
#     return render(request, 'core/teacher_list.html', context={
#         'teachers': teachers
#     })

# def teacher_details(request, pk3):
#     try:
#         teacher = Teacher.objects.get(pk=pk3)
#     except Teacher.DoesNotExist:
#         raise Http404
#     return render(request, 'core/teacher_details.html', context={
#         'teacher': teacher
#     })
