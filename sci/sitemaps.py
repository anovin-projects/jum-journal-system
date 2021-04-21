from journal.models import Manuscript, Author
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ManuscriptSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    # protocol = 'https'

    def items(self):
        return Manuscript.objects.all()

    def location(self, item):
        return reverse(item)


class AuthorSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    # protocol = 'https'

    def items(self):
        return Author.objects.all()

    def location(self, item):
        return reverse(item)
