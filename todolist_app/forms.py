from django import forms
from todolist_app.models import TaskList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class TaskForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('task'),
            Field('description'),
            Field('status'),
            Submit('submit', 'Save', css_class='btn btn-success')
        )
        
    class Meta:
        model = TaskList
        fields = ('task', 'description', 'status')
