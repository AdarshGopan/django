from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from django import forms

class OperationForm(forms.Form):
   num1=forms.IntegerField(required=True)
   num2=forms.IntegerField(required=True)

   def clean(self):
      cleaned_data=super().clean()
      n1=cleaned_data.get("num1")
      n2=cleaned_data.get("num2")
      if n1<1:
         msg="invalid value for number1"
         self.add_error("num1",msg)
      if n2<1:
         msg="invalid value for number2"
         self.add_error("num2",msg)


class OperationForm2(forms.Form):
   num=forms.IntegerField()

class operationForm3(forms.Form):
   f1=forms.CharField(label="MASTER WORD",required=True)
   f2=forms.CharField(label="CHECK  WORD",required=True)


class AddView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        
        form=OperationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)+int(n2)
            return render(request,"add.html",{"result":res})
        else:
            return render(request,"add.html",{"form":form})
         # print(request.POST)
      #   n1=request.POST["num1"]
      #   n2=request.POST['num2']
      #   res=int(n1)+int(n2)
         #   print("result=",res)
      #   return render(request,"add.html",{"result":res})
        

class SubView(View):
     def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})
     def post(self,request,*args,**kwargs):
         form=OperationForm(request.POST)

         if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)-int(n2)
            return render(request,"sub.html",{"result":res})
         else:
            return render(request,"sub.html",{"form":form})
         # print(request.POST)
      #   n1=request.POST["num1"]
      #   n2=request.POST['num2']
      #   res=int(n1)-int(n2)
      #   print("result=",res)
         #   return render(request,"sub.html",{"result":res})
    
class MulView(View):
     def get(self,request,*args,**kwargs):
        f=OperationForm()
        return render(request,"mul.html",{"form":f})
     def post(self,request,*args,**kwargs):
         # print(request.POST)
        n1=request.POST["num1"]
        n2=request.POST['num2']
        res=int(n1)*int(n2) 
      #   print("result=",res)
        return render(request,"mul.html",{"result":res})

class CubeView(View):
     def get(self,request,*args,**kwargs):
        form=OperationForm2()
        return render(request,"cube.html",{"form":form})
     def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        res=n**3
      #   print("result=",res)
        return render(request,"cube.html",{"result":res})

class EvenOddView(View):
     def get(self,request,*args,**kwargs):
        f=OperationForm2()
        return render(request,"evenodd.html",{"form":f})
     def post(self,request,*args,**kwargs):
        n=request.POST["num"]
      #   print(n)
        if n % 2 == 0:
          a=" is an Even Number"
        else:
          a=" is an Odd Number"
        return render(request,"evenodd.html",{"result":a,"value":n})

class PrimeNumberView(View):
     def get(self,request,*args,**kwargs): 
        form=OperationForm2()
        return render(request,"prime.html",{"form":form})
     def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        for i in range(2,n):
         if n % i == 0:
            a=" is not a prime number"
            break
         else:
            a=" is a prime number"
            break
        return render(request,"prime.html",{"result":a,"value":n})

class FactorialView(View):
     def get(self,request,*args,**kwargs):
        form=OperationForm2()
        return render(request,"fact.html",{"form":form})
     def post(self,request,*args,**kwargs):
        n=int(request.POST["num"])
        fact=1
        for i in range(1,n+1):
         fact=fact*i 
         f="factorial result="
      #   print("factorial of ",n,"is ",fact)
        return render(request,"fact.html",{"f":f,"result":fact})


class PatternCheckView(View):
     def get(self,request,*args,**kwargs):
      f=operationForm3()
      return render(request,"patterncheck.html",{"form":f}) 
     def post(self,request,*args,**kwargs):
      form=operationForm3(request.POST)
      if form.is_valid():
         w1=form.cleaned_data.get("f1")
         w2=form.cleaned_data.get("f2")
         p=0
         for i in w2:
            if w2.count(i)>w1.count(i):
               p=1
         if p==0:
            res="TRUE"
         else:
            res="FALSE"
      return render(request,"patterncheck.html",{"result":res,"form":form})

  