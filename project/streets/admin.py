from django.contrib import admin
from .models import Posts, ImagesPost, Categories
from .forms import AddPostForm


class PostsAdmin(admin.ModelAdmin):
	form = AddPostForm
	class Media:
		css = {
            "all": ["admin/css/admin_custom.css"],
        }

class CategoriesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(ImagesPost)
admin.site.register(Categories, CategoriesAdmin)