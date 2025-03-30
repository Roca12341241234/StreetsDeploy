from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Posts, Categories

posts = [
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'}
]


def index(request):
	posts = Posts.objects.filter(is_published=True)
	categories = Categories.objects.all()
	
	return render(request, 'index.html', {'categories': categories, 'posts': posts})

def post(request, post_slug):
	post = get_object_or_404(Posts, slug=post_slug)
	
	return render(request, 'post.html', {'post': post})

def category(request, category_slug):
	posts = get_object_or_404(Categories, slug=category_slug)
	posts = posts.category_posts.all()

	return render(request, 'category_posts.html', {'posts': posts})