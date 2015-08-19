from django.db import models
from django.db.models import permalink

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True, null=True)
	pub_date = models.DateTimeField()
	body = models.TextField()

	def __unicode__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('view_post', [self.slug,])