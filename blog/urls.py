from django.conf.urls import url
from . import views
from . import feeds

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<slug>[\w-]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^feeds/posts/$', feeds.PostsFeed(), name='feeds_posts'),
]