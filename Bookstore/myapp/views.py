from django.shortcuts import render,redirect
from django.urls import is_valid_path

# Create your views here.
from  django.views.generic import View
# from Bookstore.myapp.forms import BookModelForm

from myapp.forms import BookForm,BookModelForm,RegistrationForm,LoginForm

from myapp.models import books,Books
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class BookCreateView(View):

    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"add-book.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
            #<<<<<<-- b_name=form.cleaned_data.get("book_name")
            # a_name=form.cleaned_data.get("author_name")
            # prc=form.cleaned_data.get("price")-->>>>>>
            # last_book_id=books[-1].get("id")
            # id=last_book_id+1
            # new_book=form.cleaned_data
            # new_book["id"]=id
            # books.append(new_book)
            # print(books)
            # Books.objects.create(book_name=b_name,author_name=a_name,price=prc)
            form.save()
            messages.success(request,"BOOK ADDED SUCCESSFULLY")
            return redirect("book-lists")
        else:
            messages.error(request,"BOOK ADDING FAILED")
            return render(request,"add-book.html",{"form":form})
            
class BookListView(View):
    def get(self,request,*args,**kwargs):
         all_book=Books.objects.all()
         return render(request,"books-list.html",{"book":all_book})
    
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        # bk=[book for book in books if book.get("id")==id]
        bk=Books.objects.filter(id=id)
        return render(request,"book-detail.html",{"book":bk})

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        # bok=[book for book in books if book.get("id")==id].pop()
        # books.remove(bok)
        Books.objects.filter(id=id).delete()
        messages.success(request,"BOOK DELETED SUCCESSFULLY")
        return redirect("book-lists")

class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        # book=[book for book in books if book.get("id")==id].pop()
        book=Books.objects.get(id=id)
        form=BookModelForm(instance=book)
        # print(form)
        return render(request,"book-update.html",{"form":form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        form=BookModelForm(request.POST,instance=book)
        if form.is_valid():
            # data=form.cleaned_data
            # b_name=form.cleaned_data.get("book_name")
            # a_name=form.cleaned_data.get("author_name")
            # prc=form.cleaned_data.get("price")
            # id=kwargs.get("id")
            # book=[book for book in books if book.get("id")==id].pop()
            # book.update(data)
            # Books.objects.filter(id=id).update(book_name=b_name,author_name=a_name,price=prc)
            form.save()
            messages.success(request,"BOOK UPDATED SUCCESSFULLY")
            return redirect("book-lists")
        else:
            messages.error(request,"BOOK UPDATING FAILED")
            return render(request,"book-update.html",{"form":form})

        
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form = RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"REGISTRATION COMPLETED SUCCESSFULLY")
            return redirect("book-login")
        else:
            messages.error(request,"REGISTRATION FAILED !!!")
            return render(request,"registration.html",{"form":form})
        
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"LOGIN SUCCESSFULLY")
                return redirect("book-lists")
            else:
                messages.error(request,"LOGIN FAILED")
                return render(request,"login.html",{"form":form})
    
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("book-login")

    