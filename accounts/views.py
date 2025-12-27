from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

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