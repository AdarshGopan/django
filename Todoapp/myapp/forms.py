# from curses import A_ATTRIBUTES
# from tkinter import Widget
from django import forms

# from django.forms import ModelForm

from myapp.models import Todos
from django.contrib.auth.models import User

class TodoForm(forms.Form):
    task_name=forms.CharField(label="TASK NAME",required=True)
    user=forms.CharField(label="USER NAME",required=True)

class TodoModelForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields="__all__"  #"__all__" -->> to get all fields in models ["task_name","user"]

        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"})

        }
        labels={
            "task_name":"TASKNAME",
            "user":"USERNAME"
        }
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"}),
        }
        labels={
            "first_name":"FIRSTNAME",
            "last_name":"LASTNAME",
            "username":"USERNAME",
            "email":"EMAIL",
            "password":"PASSWORD",
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


      