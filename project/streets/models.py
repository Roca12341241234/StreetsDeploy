from django.db import models


class Posts(models.Model):
	title = models.CharField(verbose_name='Заголовок', max_length=255)
	description = models.TextField(verbose_name='Краткое описание')
	content = models.TextField(verbose_name='Контент')
	preview = models.ImageField(verbose_name='Картинка для превью', upload_to='photos/')
	slug = models.SlugField(verbose_name='Слаг', blank=True, null=True, default='', max_length=255, db_index=True)

	is_published = models.BooleanField(verbose_name='Опубликовать сразу', default=True)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class ImagesPost(models.Model):
	post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, null=True, related_name='images')
	image = models.ImageField(verbose_name='Картинка', upload_to=f'photos/')

	def __str__(self):
		return self.post.title

	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'