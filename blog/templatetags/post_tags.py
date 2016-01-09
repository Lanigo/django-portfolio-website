from django.template import Library
from blog.models import Post

register = Library()

@register.inclusion_tag('blog/recent_posts.html')
def get_recent_posts():
	posts = Post.objects.filter().order_by('-published_date')[:5]
	return {'posts': posts}