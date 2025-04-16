from turtle import mode
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django_extensions.db.fields import AutoSlugField

from tinymce.models import HTMLField

import pytils


class Categories(models.Model):
	name = models.CharField(verbose_name='Название категории', unique=True, max_length=255)
	slug = models.SlugField(verbose_name='Слаг', max_length=255, unique=True, db_index=True)

	def get_absolute_url(self):
		return reverse('category', kwargs={'category_slug': self.slug})

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Posts(models.Model):
	title = models.CharField(verbose_name='Заголовок', max_length=255)
	description = models.TextField(verbose_name='Краткое описание')

	content = HTMLField(verbose_name='Контент')
	preview = models.ImageField(verbose_name='Картинка для превью', upload_to='photos/')
	slug = AutoSlugField(verbose_name='Слаг',unique=True, max_length=255, db_index=True, populate_from='title', slugify_function=lambda a: pytils.translit.slugify(a))
	is_published = models.BooleanField(verbose_name='Опубликовать', default=True)

	category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name='category_posts')


	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})
	
	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'


class ImagesPost(models.Model):
	post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, null=True, related_name='images')
	image = models.ImageField(verbose_name='Картинка', upload_to='photos/')


	def __str__(self):
		return self.post.title
	
	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'

class VideosPost(models.Model):
	post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, null=True, related_name='videos')
	video = models.FileField(verbose_name='Видео', upload_to='videos/')
	description = models.TextField(verbose_name='Краткое описание видео(необязательно)', max_length=255, blank=True, null=True)

	def __str__(self):
		return self.post.title

	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'