from turtle import mode
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django_extensions.db.fields import AutoSlugField

from tinymce.models import HTMLField

import pytils


class Category(models.Model):
	name = models.CharField(verbose_name='Название категории', unique=True, max_length=255)
	slug = models.SlugField(verbose_name='Слаг', max_length=255, unique=True, db_index=True)

	def get_absolute_url(self):
		return reverse('category', kwargs={'category_slug': self.slug})

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Post(models.Model):
	title = models.CharField(verbose_name='Заголовок', max_length=255)
	description = models.TextField(verbose_name='Краткое описание')

	content = HTMLField(verbose_name='Контент')
	preview = models.ImageField(verbose_name='Картинка для превью', upload_to='photos/')
	date_create = models.DateField(verbose_name='Дата создания поста', auto_now_add=True)
	date_update = models.DateField(verbose_name='Дата обновления поста', auto_now=True)
	views = models.IntegerField(verbose_name='Просмотры', default=0)
	video = models.FileField(verbose_name='Видео', upload_to='videos/')
	slug = AutoSlugField(
		verbose_name='Слаг',
		unique=True,
		max_length=255, 
		db_index=True, 
		populate_from='title', 
		slugify_function=lambda a: pytils.translit.slugify(a))
	is_published = models.BooleanField(verbose_name='Опубликовать', default=True)

	category = models.ForeignKey(verbose_name='Категория поста', 
							  to=Category, 
							  on_delete=models.CASCADE, 
							  related_name='category_posts')


	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})
	
	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

