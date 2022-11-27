"""sci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import volumeview

urlpatterns = [
    path('', views.index, name='index'),
    path('abstract/<slug_field>/', views.abstract, name='abstract-detail'),
    path('author/<id>/', views.author, name='author'),
    path('volume/<name>', volumeview, name='volume_view'),
    path('thanks/', views.thanks, name='thanks'),
    path('report/', views.report, name='report'),
    path('contact/', views.contact, name='contact'),
    path('advanced-search/', views.advancedsearch, name='advanced_search'),
    path('api/', include('journal.apiurls'))
]
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
