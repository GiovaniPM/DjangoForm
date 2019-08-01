#-*- coding: utf-8 -*-
from myapp.forms import LoginForm
def login(request):
 username = "not logged in"
 if request.method == "POST":
 #Get the posted form
 MyLoginForm = LoginForm(request.POST)
 if MyLoginForm.is_valid():
 username = MyLoginForm.cleaned_data['username']
 else:
 MyLoginForm = Loginform()
 return render(request, 'loggedin.html', {"username" : username})