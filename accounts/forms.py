from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=200,widget=TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(max_length=200,widget=EmailInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(max_length=200,widget=TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=200,widget=TextInput(attrs={'placeholder':'Last Name'}))
    password_1 = forms.CharField(max_length=200,widget=PasswordInput(attrs={'placeholder':'Password'}))
    password_2 = forms.CharField(max_length=200,widget=PasswordInput(attrs={'placeholder':'Confirm Password'}))

    def clean_username(self):
        # تعریف و ریختن مقداری که کاربر وارد کرده (به عنوان ولیو از لیست کیلیند دیتا) داخل متغیر یوزر
        username = self.cleaned_data['username']
        # از طریف مدیر بخش دیتا بیس یا همون مدل (آبجکتس) پیدا کردن یوزرنیم تکراری
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already taken')
        return email

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 != password_2:
            raise forms.ValidationError('Passwords must match')
        elif len(password_1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        elif not any (x.isupper for x in password_1):
            raise forms.ValidationError('Password must be at least one uppercase letter')
        return password_1

class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)