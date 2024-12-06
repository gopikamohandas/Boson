from django import forms
from .models import Todo


class Dateinput(forms.DateInput):
    input_type= ('date')

class TodoForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields = ('__all__')


widgets = {            
            'Deadline': Dateinput(attrs={'class': 'datepicker'})
        }