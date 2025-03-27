from django.shortcuts import render, HttpResponse


posts = [
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'},
	{'title': 'Test1', 'img': '', 'description': 'test descriptiondsfsdfsf sdfsdfsdfdfsdf sd sf sdf sfsdf sdfsdfsdf sdf sdf sdf sdf sdf sfdsd fsd'}
]


def index(request):
	return render(request, 'index.html', {'posts': posts})