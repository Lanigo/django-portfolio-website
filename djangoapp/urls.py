from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', 'thesite.views.home', name='home'),
	url(r'^contact/$', 'thesite.views.contact', name='contact'),
    url(r'^thanks/$', 'thesite.views.thanks', name='thanks'),
    url(r'^about/$', 'thesite.views.about', name='about'),
    url(r'^projects/$', 'thesite.views.projects', name='projects'),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
