from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


from users.forms import UserLoginForm

from cash.models import Money

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(form.errors)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
        print(form.errors)

    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
