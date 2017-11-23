from django import forms
from .models import Question

class QuestionListForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('pub_date', 'Дата публикации'), ('autor', 'Автор'), ('category', 'Категория')))

#class QuestionForm(forms.ModelForm):
#    
#    class Meta:
#        model = Question
    
