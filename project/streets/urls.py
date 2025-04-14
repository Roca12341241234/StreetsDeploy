from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('post/<slug:post_slug>', views.post, name='post'),
	path('category/<slug:category_slug>', views.category, name='category'),
	path('add_post/', views.add_post, name='add_post'),

]
