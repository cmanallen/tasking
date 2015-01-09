from django import forms
from teams.models import Team


class CreateUserTask(forms.ModelForm):
  model = Team
  fields = ('user_team', 'id')