from django.db import models


class Posts(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()

	is_published = models.BooleanField(default=True)