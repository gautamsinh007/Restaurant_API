from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cat_Res,Restaurant,Iteams
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','first_name','last_name']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields='__all__'


class Cat_resSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cat_Res
        fields='__all__'
   
class IteamSSerializer(serializers.ModelSerializer):
    class Meta:
        model=Iteams
        fields='__all__'


# ---------for 1. Query
class ListCatSerializer(serializers.ModelSerializer):
    res=RestaurantSerializer()
    class Meta:
        model=Cat_Res
        fields=['id','cat_name','restaurant']

class IteamListSerializer(serializers.ModelSerializer):
    cat = ListCatSerializer()
    
    class Meta:
        model=Iteams
        fields=['id','iteam_name','category','price']


#--------for 2. Query...
class CustomeIteamSSerializer(serializers.ModelSerializer):
    # cat = Cat_resSerializer()
    #restaurant = serializers.ReadOnlyField(source='cat.cat_name')
    restaurant=serializers.SerializerMethodField()
    class Meta:
        model=Iteams
        fields=['iteam_name','restaurant']

    def get_restaurant(self, instance):
        #print(instance.cat.res, "?????")
        return instance.category.restaurant.res_name

#--------for 3. Query--------------
class all_iteam_with_cat_using_res_Serializer(serializers.ModelSerializer):
    category=Cat_resSerializer()
    class Meta:
        model=Iteams
        fields=['category','iteam_name','price','available']



#--------for 4. Query--------------
class Restaurant_details_with_count_Serializer(serializers.ModelSerializer):
    total_count=serializers.SerializerMethodField()
    class Meta:
        model=Restaurant
        fields=['res_name','total_count']
    def get_total_count(self,instance):
        return Iteams.objects.filter(restaurant=instance).count()
    

#--------for 5. Query--------------



#--------for 6. Query--------------
class Res_Greater_500_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields=['res_name']


    
