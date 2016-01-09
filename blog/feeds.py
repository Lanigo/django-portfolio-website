from django.contrib.syndication.views import Feed
from .models import Post
from django.core.urlresolvers import reverse

class PostsFeed(Feed):
	title = "My Blog Posts"
	link = "feeds/posts/"
	description = "Posts from My Blog"

	def items(self):
		return Post.objects.order_by('-published_date')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text