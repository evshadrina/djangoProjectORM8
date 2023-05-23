from django import forms
''''
class FeedbackForm(forms.Form):
    name=forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
        'max_length': 'Слишклм длтинное имя',
        'min_length':' Сдишком коротнлое имя',
        'required': 'Укажите хотя б 2 символа'

    })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20}))

'''
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields ='__all__'
        #fields = ('title', 'text',)
        labels={
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
        }