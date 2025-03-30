from django.db import models
from django.urls import reverse


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
	content = models.TextField(verbose_name='Контент')
	preview = models.ImageField(verbose_name='Картинка для превью', upload_to='photos/')
	slug = models.SlugField(verbose_name='Слаг', unique=True, max_length=255, db_index=True)

	category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name='category_posts')

	is_published = models.BooleanField(verbose_name='Опубликовано?', default=True)

	def __str__(self):
		return self.title
	

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})
	

class ImagesPost(models.Model):
	post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, null=True, related_name='images')
	image = models.ImageField(verbose_name='Картинка', upload_to=f'photos/')

	def __str__(self):
		return self.post.title


	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'

