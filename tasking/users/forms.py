from django import forms
from users.models import User

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	def save(self):
		user = super(UserRegisterForm, self).save()
		user.set_password(self.cleaned_data['password'])
		user.save()
		return user

	class Meta:
		model = User
		fields = ('username', 'email', 'password')