from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    id=models.IntegerField(primary_key=True)
    res_name=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='res_owner')
    
    def __str__(self) -> str:
         return self.res_name

class Cat_Res(models.Model):
    id=models.IntegerField(primary_key=True)
    cat_name=models.CharField(max_length=50)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='res_cat')
    
    def __str__(self):
	    return self.cat_name+self.restaurant.res_name

class Iteams(models.Model):
    id=models.IntegerField(primary_key=True)
    iteam_name=models.CharField(max_length=50)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='res_iteam')
    category=models.ForeignKey(Cat_Res,on_delete=models.CASCADE)
    price=models.FloatField()
    available=models.BooleanField(default=True)
    


