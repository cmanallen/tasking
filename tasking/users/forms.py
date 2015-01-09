from django import forms

from .models import User


class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	def save(self):
		user = super(UserRegisterForm, self).save()
		user.set_password(self.cleaned_data['password'])
		user.save()
		return user

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password', 'avatar')


class UserUpdateForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'first_name',
			'last_name',
			'avatar',
		)


class UserChangePasswordForm(forms.ModelForm):
	
	def save(self):
		user = super(UserChangePasswordForm, self).save()
		user.set_password(self.cleaned_data['new_password'])
		user.save()
		return user

	class Meta:
		model = User