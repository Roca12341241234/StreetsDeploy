from django.contrib import admin
from .models import Posts, ImagesPost, Categories


class PostsAdmin(admin.ModelAdmin):
	pass
	# fields = ['title', 'description', 'content', 'preview', 'category', 'is_published']
	# prepopulated_fields = {'slug': ('title',)}

class CategoriesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(ImagesPost)
admin.site.register(Categories, CategoriesAdmin)