from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = MarkdownField()
	slug = models.SlugField(default=0)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = TaggableManager()
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
