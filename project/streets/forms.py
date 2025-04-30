from django import forms
from .models import Posts, Categories

from project.settings import allowed_extensions_for_video_files


class AddPostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = '__all__'
	
	def clean_video(self):
		video_file = self.cleaned_data.get('video')
		if video_file:
			
			ext = video_file.name.lower().rsplit('.', 1)[-1]

			if f'.{ext}' not in allowed_extensions_for_video_files:
				raise forms.ValidationError("Разрешены только видеофайлы (MP4, MOV, AVI, MKV).")
			
		return video_file