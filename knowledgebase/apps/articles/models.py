from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Article(models.Model):
	category_choices = (
		('InTouch', 'InTouch'),
		('System Platform', 'System Platform'),
		('Workflow', 'Workflow'),
	)

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	category = models.CharField(max_length=20
		,choices=category_choices
		,default='InTouch')
	slug = models.SlugField(blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)	

	def __str__(self):
		return self.title


