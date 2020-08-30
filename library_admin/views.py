from django.shortcuts import render
from . import forms
# Create your views here.
def homePage(request):
	return render(request,'library_admin/home.html')

def AdminLogin(request):
	form = forms.AdminLoginForm()
	if request.method == 'POST':
		form=forms.AdminLoginForm(request.POST)
	return render(request, 'library_admin/logs/login.html', {'form': form})
