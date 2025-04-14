from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from django.utils.text import slugify

from .models import Posts, Categories, ImagesPost
from .forms import AddPostForm


def index(request):
	posts = Posts.objects.filter(is_published=True)
	categories = Categories.objects.all()

	return render(request, 'index.html', {'categories': categories, 'posts': posts, 'scroll': True})

def post(request, post_slug):
	_post = Posts.objects.get(slug=post_slug)
	images = ImagesPost.objects.filter(post = _post)
	
	return render(request, 'post.html', {'post': _post, 'images': images, 'scroll': True})

def category(request, category_slug):
	posts = get_object_or_404(Categories, slug=category_slug)
	posts = posts.category_posts.all()

	return render(request, 'category_posts.html', {'posts': posts, 'scroll': True})

def add_post(request):
	if request.method == 'POST':
		form = AddPostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			redirect('index')
	else:
		form = AddPostForm()

	return render(request, 'add_post.html', {'form': form, 'scroll': False})

def upload_video(request):
	video = request.FILES.upload_files[0]