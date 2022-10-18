# from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
todos=[

    {"id":1,"task_name":"gbillpay","user":"ram"},
    {"id":2,"task_name":"task2","user":"ravi"},
    {"id":3,"task_name":"task3","user":"amal"},
    {"id":4,"task_name":"task4","user":"ambu"},
    {"id":5,"task_name":"task5","user":"sanju"},
    {"id":6,"task_name":"task6","user":"manu"},

]

class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.CharField(max_length=200)

#ORM -> object relational mapping 
#create
#list
#update
#delete
#detail

#orm query for create object
# modelName.objects.create(field1=value1,field2=value2,fieldn=valuen)
# Todos.objects.create(task_name="mobilebill",user="ravi")

#ORM QUERY FOR FETCH ALL RECORDS
# qs=Todos.objects.all()
# print([todo.task_name for todo in qs])

# ORM QUERY FOR FETCH SINGLE OBJECT
# qs=Todos.objects.get(id=3)
# print(qs.task_name)

# ORM QUERY FOR FILTERING MULTIPLE OBJECTS
# qs=Todos.objects.filter(user="ravi")
# print([todo.task_name for todo in qs])
# print([todo.user for todo in qs])

# ORM QUERY FOR UPDATE SPECIFIC OBJECT
# Todos.objects.filter(id=3).update(task_name="electricityBill")
 
#ORM QUERY FOR DELETE SPECIFIC OBJECT
# Todos.objects.filter(id=2).delete()