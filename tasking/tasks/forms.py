from django import forms
from tasks.models import Task

class CreateTask(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('name', 'status', 'task_type', 'description', 'due')