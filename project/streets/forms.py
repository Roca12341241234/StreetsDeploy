from django import forms
from .models import Posts, Categories


class AddPostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ['title', 'description', 'content', 'preview', 'category']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form_item form_input'}),
			'description': forms.Textarea(attrs={
				'class': 'form_item form_description'
			}),
			'content': forms.Textarea(attrs={
				'class': 'form_item form_content',
				'rows': '30'
			}),
			'category': forms.Select(attrs={'class': 'form_item'}),

		}