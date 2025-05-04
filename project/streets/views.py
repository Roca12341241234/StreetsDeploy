from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from django.utils.text import slugify

from .models import Posts, Categories, ImagesPost
from .forms import AddPostForm, PostFilterForm


def index(request):
	posts = Posts.objects.filter(is_published=True)
	categories = Categories.objects.all()

	return render(request, 'index.html', {'categories': categories, 'slider_posts': posts[:5], 'scroll': True})

def post(request, post_slug):
	_post = Posts.objects.get(slug=post_slug)
	_post.views+=1
	_post.save()

	return render(request, 'post.html', {'post': _post, 'scroll': True})

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

def posts(request):
	_posts = Posts.objects.get_queryset()
	filters_form = PostFilterForm(data=request.GET)

	if filters_form.is_valid():
		category = filters_form.cleaned_data.get('category')
		date = filters_form.cleaned_data.get('date')
		views = filters_form.cleaned_data.get('views')
		search_query = filters_form.cleaned_data.get('search_query')

		if search_query:
			_posts = _posts.filter(title__icontains=search_query)

		if category:
			_posts = _posts.filter(category=category)

		if date == '0':
			_posts = _posts.order_by('-date_create')
		elif date == '1':
			_posts = _posts.order_by('date_create')

		if views == '0':
			_posts = _posts.order_by('-views')
		elif views == '1':
			_posts = _posts.order_by('views')

	
	return render(request, 'posts.html', {'filters_form': filters_form, 'posts': _posts, 'scroll': False})