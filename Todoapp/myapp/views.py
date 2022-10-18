from email import message
from urllib import request
from django.shortcuts import render,redirect

# Create your views here.
from myapp.forms import TodoForm,TodoModelForm,RegistrationForm,LoginForm

from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from myapp.models import todos,Todos
from django.contrib import messages

class TodoCreateView(View):
     def get(self,request,*args,**kwargs):
        form=TodoModelForm()
        return render(request,"add-todo.html",{"form":form})
    
     def post(self,request,*args,**kwargs):
        form=TodoModelForm(request.POST)
        if form.is_valid():
            # t_name=form.cleaned_data.get("task_name")
            # usr=form.cleaned_data.get("user")
            # Todos.objects.create(task_name=t_name,user=usr)
            form.save()
            messages.success(request,"TODO CREATING SUCESSFULLY")
            return redirect("todo-list")

        else:
            messages.error(request,"TODO CREATING FAILED")
            return render(request,"add-todo.html",{"form":form})


class TodoListView(View):
    def get(self,request,*args,**kwargs):
        all_todos=Todos.objects.all()
        return render(request,"todo-list.html",{"todos":all_todos})
     
class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        i_d=kwargs.get("id")
        # todo=[todo for todo in todos if todo.get("id")==id ]
        todo=Todos.objects.filter(id=i_d)
        return render(request,"todo-detail.html",{"todo":todo})

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        i_d=kwargs.get("id")
        # todo=[todo for todo in todos if todo.get("id")==id ].pop()
        Todos.objects.filter(id=i_d).delete()
        # Todos.remove(todo)
        messages.success(request,"TODO DELETED SUCCESSFULLY")
        return redirect("todo-list")   

class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        # todo=[todo for todo in todos if todo.get("id")==id ].pop()
        todo=Todos.objects.get(id=id)
        form=TodoModelForm(instance=todo)
        return render(request,"todo-update.html",{"form":form})  
   
   
    def post(self,request,*args,**kwargs):
        i_d=kwargs.get("id")
        todo=Todos.objects.get(id=i_d)
        form=TodoModelForm(request.POST,instance=todo)
        if form.is_valid():
            # t_name=form.cleaned_data.get("task_name")
            # usr=form.cleaned_data.get("user")
            # i_d=kwargs.get("id")
            # todo=[todo for todo in todos if todo.get("id")==id ].pop()
            # todo.update(data)
            # Todos.objects.filter(id=i_d).update(task_name=t_name,user=usr) #(**form.cleaneddata)
            form.save()
            messages.success(request,"TODO UPDATED SUCCESSFULLT")
            return redirect("todo-list")
        else:
            messages.error(request,"TODO UPDATING FAILED")
            return render(request,"todo-update.html",{"form":form})


class RegistrationView(View):
    def get(self,request,*args,**kw):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kw):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"REGISTRATION COMPLETED SUCCESSFULLY")
            return redirect("todo-login")
        else:
            messages.error(request,"REGISTRATION FAILED")
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
                return redirect("todo-list")
            else:
                messages.error(request,"LOGIN FAILED")
                return render(request,"login.html",{"form":form})

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("todo-login")