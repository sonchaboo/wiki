"""ozon_wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core.views import main, categ_list, article_list, article


urlpatterns = [
    path('main/', main, name='main'),
    path('categ_list/<int:pk>/', categ_list, name='categ_list'),
    # path('topic2/<int:pk2>/', topic_details2, name='topic_details2'),
    # path('teachers/', teacher_list, name='teacher_list'),
    path('article_list/<int:pk2>/', article_list, name='article_list'),
    path('articles/<int:pk3>/', article, name='article'),
    # path('news/', news, name='news'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
