
from django import forms
from .models import LoginModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200  ,  widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-green-600 focus:border-green-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        })
    )
    password = forms.CharField(max_length=100 ,  widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-green-600 focus:border-green-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        })
    )