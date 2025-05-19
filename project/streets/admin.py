from django.contrib import admin
from .models import Post, Category
from .forms import AddPostForm


class PostsAdmin(admin.ModelAdmin):
	form = AddPostForm
	class Media:
		css = {
            "all": ["admin/css/admin_custom.css"],
        }

class CategoriesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostsAdmin)
admin.site.register(Category, CategoriesAdmin)