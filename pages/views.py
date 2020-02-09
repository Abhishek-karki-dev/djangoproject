from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    # data = [{
    #     'id':1,
    #     'name':'Ram'
    # },
    # {
    #     'id':2,
    #     'name':'Hari'
    # }]
    # context = {'data':data}
    return render(request, 'index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        forms = SignUpForm()
    return render(request, 'registration/signup.html',{'forms':forms})


def login(request):
    return render(request, 'login.html')
