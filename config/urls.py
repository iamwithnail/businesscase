# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from core import views as cv



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'costs/$', TemplateView.as_view(template_name='core/costform.html'), name='costs'),
    url(r'risks/$', TemplateView.as_view(template_name='core/risks.html'), name='risks'),
    url(r'benefits/graph/$', TemplateView.as_view(template_name='core/benefits-graph.html'), name='benefits-summary'),
    url(r'summary/', TemplateView.as_view(template_name='core/summary-graph.html'), name='summary'),
    url(r'funding/graph/', cv.funding, name='funding-summary'),
    url(r'benefits/$', TemplateView.as_view(template_name='core/benefits.html'), name='benefits'),
    url(r'economics/$', TemplateView.as_view(template_name='core/economic-summary.html'), name='economics'),
    url(r'dashboard/$', TemplateView.as_view(template_name='core/dashboard.html'), name='dashboard'),
    url(r'testendpoint/$', cv.cost_items),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('businesscase.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
