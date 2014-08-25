from django import forms
from tasks.models import Task, Comment

class TaskForm(forms.ModelForm):
	due = forms.DateField(widget=forms.TextInput(
		attrs={
			'class': 'datepicker',
			'data-date-format': 'yyyy-mm-dd',
		}
	))

	class Meta:
		model = Task
		fields = ('project', 'name', 'due', 'priority', 'task_type', 'description', 'created_by')

class TaskCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body', 'task', 'user')
