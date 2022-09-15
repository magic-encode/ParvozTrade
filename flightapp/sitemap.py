from django.contrib.sitemaps import Sitemap
from flightapp.models.products import Products

from datetime import datetime


class PageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    def items(self):
        page = Products.objects.all()
        return page
    def lastmod(self, obj):
        return obj.updated

