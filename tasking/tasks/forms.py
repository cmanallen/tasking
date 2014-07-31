from django import forms
from tasks.models import Task, Comment

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('project', 'name', 'status', 'task_type', 'description', 'due', 'created_by')

class TaskCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)