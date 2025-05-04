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
	
class PostFilterForm(forms.Form):
	search_query = forms.CharField(
		label='Поиск по заголовку',
		required=False,
		max_length=255,
		widget=forms.TextInput(attrs={'placeholder': 'Введите сюда запрос...'})
	)
	date = forms.ChoiceField(
		required=False, 
		label="По дате",
		choices=[("", "Не выбрано"), (0, 'По убыванию'), (1, 'По возрастанию')],
		widget=forms.Select(attrs={'class': 'filters-by-date'})
	)
	views = forms.ChoiceField(
		required=False, 
		label="По просмотрам",
		choices=[("", "Не выбрано"), (0, 'По убыванию'), (1, 'По возрастанию')],
		widget=forms.Select(attrs={'class': 'filters-by-views'})
	)
	category = forms.ChoiceField(
		required=False,
		label="Категория",
		choices=[("", "Все")] + [(cat.id, cat.name) for cat in Categories.objects.all()],
		widget=forms.Select(attrs={'class': 'filters-by-category'})
	)