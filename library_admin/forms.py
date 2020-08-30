from django import forms

class AdminLoginForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
