from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from django.utils.text import slugify
from django.forms.models import model_to_dict

from .models import Posts, Categories, ImagesPost
from .forms import AddPostForm, PostFilterForm
from config.models import DefaultConfig, Participants

try:
	default_config = DefaultConfig.objects.get()
	default_context = model_to_dict(default_config)
except:
	default_context = {}


def index(request):
	posts = Posts.objects.filter(is_published=True)
	categories = Categories.objects.all()

	return render(request, 'index.html', {**default_context, 'categories': categories, 'posts': posts[:5], 'scroll': True})

def post(request, post_slug):
	_post = Posts.objects.get(slug=post_slug)
	_post.views+=1
	_post.save()

	return render(request, 'post.html', {**default_context, 'post': _post, 'scroll': False})

def category(request, category_slug):
	posts = get_object_or_404(Categories, slug=category_slug)
	posts = posts.category_posts.all()

	return render(request, 'category_posts.html', {**default_context, 'posts': posts, 'scroll': True})

def add_post(request):
	if request.method == 'POST':
		form = AddPostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			redirect('index')
	else:
		form = AddPostForm()

	return render(request, 'add_post.html', {**default_context, 'form': form, 'scroll': False})

def posts(request):
	_posts = Posts.objects.all()
	filters_form = PostFilterForm(data=request.GET)

	if filters_form.is_valid():
		category = filters_form.cleaned_data.get('category')
		date = filters_form.cleaned_data.get('date')
		views = filters_form.cleaned_data.get('views')
		search_query = filters_form.cleaned_data.get('search_query')

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

		if search_query:
			_posts = _posts.filter(title__icontains=search_query)

	
	return render(request, 'posts.html', {**default_context, 'filters_form': filters_form, 'posts': _posts, 'scroll': False})

def about(request):
	participants = Participants.objects.all()

	return render(request, 'about.html', {**default_context, 'participants': participants})