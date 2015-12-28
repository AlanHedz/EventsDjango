from django import forms
from .models import Event, Comments

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('views','created','modified','organizer')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
			'category': forms.Select(attrs={'class': 'form-control'}),
			'place': forms.TextInput(attrs={'class': 'form-control'}),
			'start': forms.DateTimeInput(attrs={'class': 'form-control'}),
			'finish': forms.DateTimeInput(attrs={'class': 'form-control'}),
			'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'is_free': forms.CheckboxInput(attrs={'class': 'form-control'}),
			'amoun': forms.NumberInput(attrs={'class': 'form-control'}),
		}
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = {'user','event'}
        widgets = {
        	'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'})
        }

    