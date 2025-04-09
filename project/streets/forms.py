from django import forms
from .models import Posts, Categories


class AddPostForm(forms.Form):
	title = forms.CharField(label='Название', max_length=255)
	description = forms.CharField(label='Описание', widget=forms.Textarea)
	content = forms.CharField(label='Контент', widget=forms.Textarea)
	preview = forms.ImageField(label='Превью поста')
	category = forms.ModelChoiceField(queryset=Categories.objects.all())