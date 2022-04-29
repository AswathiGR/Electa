from django.db import models

# Create your models here.
from django.db import models  
class Voters_list(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)
    efingerid=models.CharField(max_length=15) 
    eaddress = models.CharField(max_length=150)  
    class Meta:  
        db_table = "voters_list"  
