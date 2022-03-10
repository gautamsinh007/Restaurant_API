from django.contrib import admin
from .models import Restaurant,Cat_Res,Iteams

@admin.register(Restaurant)
class Restaurantadmin(admin.ModelAdmin):
    list_display=['id','res_name','city','owner']
@admin.register(Cat_Res)
class Cat_res_admin(admin.ModelAdmin):
    list_display=['id','cat_name','restaurant']
@admin.register(Iteams)
class Iteamsadmin(admin.ModelAdmin):
    list_display=['id','iteam_name','category','price','available','restaurant']

