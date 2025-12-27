from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'], email=data['email'],
                                     first_name=data['first_name'],last_name=data['last_name'],
                                     password=data['password_2'])
            return redirect('home:home')
        return render(request,'accounts/register.html',{'form': form})

    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(username=User.objects.get(email=data['user']), password=data['password'])
            except:
                user = authenticate(username=data['user'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home:home')
        else:
            return render(request, 'accounts/login.html', {'form': form})

    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')
