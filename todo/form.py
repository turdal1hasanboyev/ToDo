from django import forms
from .models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['updated_at', 'created_at', 'is_done']
        widgets = {
            'deadline': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field.widget.attrs, "Field")

            if field_name == 'is_done':
                field.widget.attrs['class'] = ''
            else:
                field.widget.attrs['class'] = 'form-control'
                
            # field.widget.attrs['placeholder'] = field_name
