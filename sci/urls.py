from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from journal.models import Manuscript
from . import views
from schema_graph.views import Schema
import debug_toolbar

info_dict = {
    'queryset': Manuscript.objects.all(),
}

admin.AdminSite.site_header = 'Biology Students\' Research Society Administration Panel'
admin.AdminSite.site_title = 'ИДСБ'

urlpatterns = [
    path('', include('journal.urls')),
    path('', include('pwa.urls')),
    path('secret/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('tinymce/', include('tinymce.urls')),
    path('static', static),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'manuscripts': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path("schema/", Schema.as_view()),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
