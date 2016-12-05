from django import forms  
from django.contrib.auth import(
		authenticate,
		get_user_model,
		login,
		logout
	)
from django.contrib import auth
from django.contrib.auth.models import User

User = get_user_model()

class UserLoginForm(forms.Form):  
    username = forms.CharField()      
    password = forms.CharField(widget=forms.PasswordInput)  

    def clean(self, *args, **kwargs):

    	if self.cleaned_data.get("username") and self.cleaned_data.get("password"):
    		user = authenticate(username=self.cleaned_data.get("username"), passowrd=self.cleaned_data.get("password"))
    		print (user)
	    	if not user:
	    		raise forms.ValidationError("The user does not exist")
	    	if not user.check_password(password):
	    		raise forms.ValidationError("Incorrect password")
	    	return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	firstname = forms.CharField(label='First Name')
	lastname = forms.CharField(label='Last Name')

	def clean(self):
		if User.objects.filter(username = self.cleaned_data.get("username")).exists():
			raise forms.ValidationError("Username already taken")

    


