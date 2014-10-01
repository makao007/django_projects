from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'renwu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'novel.views.index'),
    url(r'^n/(\d+)', 'novel.views.novel'),
    url(r'^t/(\d+)', 'novel.views.tag'),
    url(r'^c/(\d+)', 'novel.views.category'),
    url(r'^s/(.*)', 'novel.views.name'),

)
