from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sofomweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('sofomweb.apps.home.urls')),
)
