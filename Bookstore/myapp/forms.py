
from django import forms
from myapp.models import Books
from django.contrib.auth.models import User
class BookForm(forms.Form):
    book_name=forms.CharField(label=" BOOK  NAME ",required="true")
    author_name=forms.CharField(label="AUTHOR NAME",required="true")
    price=forms.CharField(label="SELLING PRICE",required="true") 

class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"})
            }
        labels={
            "book_name":"BOOK NAME:",
            "author_name":"AUTHOR NAME",
            "price":"PRICE"
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
            "email":"EMAIL ADDRESS",
            "password":"PASSWORD",
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))