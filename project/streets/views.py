from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Posts

posts = [
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'}
]


def index(request):
	posts = Posts.objects.all()
	return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
	post = get_object_or_404(Posts, pk=post_id)
	
	return render(request, 'post.html', {'post': post})