from django.db import models

# Create your models here.

books=[
    {"id":1,"book_name":"meenu","author_name":"ravi","price":1378},
    {"id":2,"book_name":"mathilukal","author_name":"basheer","price":3378},
    {"id":3,"book_name":"Harry Potter","author_name":"murali","price":1238},
    {"id":4,"book_name":"malaka","author_name":"moorthy","price":1300},
    {"id":5,"book_name":"megham","author_name":"gayathri","price":1400},

]

class Books(models.Model):
    book_name=models.CharField(max_length=200)
    author_name=models.CharField(max_length=200)
    price=models.PositiveIntegerField(default=500)


