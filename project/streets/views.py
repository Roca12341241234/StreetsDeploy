from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from django.utils.text import slugify

from .models import Posts, Categories, ImagesPost
from .forms import AddPostForm

posts = [
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'}
]


def index(request):
	posts = Posts.objects.filter(is_published=True)
	categories = Categories.objects.all()

	print(posts[0].preview.__dict__)
	
	return render(request, 'index.html', {'categories': categories, 'posts': posts})

def post(request, post_slug):
	_post = Posts.objects.get(slug=post_slug)
	images = ImagesPost.objects.filter(post = _post)
	print(images[0].__dict__)
	
	return render(request, 'post.html', {'post': _post, 'images': images})

def category(request, category_slug):
	posts = get_object_or_404(Categories, slug=category_slug)
	posts = posts.category_posts.all()

	return render(request, 'category_posts.html', {'posts': posts})

def add_post(request):
	if request.method == 'POST':
		form = AddPostForm(request.POST, request.FILES)
		if form.is_valid():
			# slug = slugify(form.cleaned_data['title'], allow_unicode=True)
			new_post = Posts(
				title=form.cleaned_data['title'],
				description=form.cleaned_data['description'],
				content=form.cleaned_data['content'],
				preview=form.cleaned_data['preview'],
				category=form.cleaned_data['category']
			)
			print(form.cleaned_data)
			new_post.save()

			# return HttpResponseRedirect('/add_post/')
	else:
		form = AddPostForm()

	return render(request, 'add_post.html', {'form': form})