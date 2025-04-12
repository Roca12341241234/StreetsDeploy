from django import forms
from .models import Posts, Categories



class AddPostForm(forms.ModelForm):
	class Meta:
		model = Posts
		# content = forms.CharField(widget=CKEditorWidget())
		fields = '__all__'
		# fields = ['title', 'description', 'content', 'preview', 'category']
		# widgets = {
		# 	'title': forms.TextInput(attrs={'class': 'form_item form_input'}),
		# 	'description': forms.Textarea(attrs={
		# 		'class': 'form_item form_description'
		# 	}),
		# 	# 'content': forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor')),
		# 	'category': forms.Select(attrs={'class': 'form_item'}),
			
		# }