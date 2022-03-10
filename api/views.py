from urllib import response
from rest_framework.generics import GenericAPIView
from .models import Restaurant,Cat_Res,Iteams
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import all_iteam_with_cat_using_res_Serializer,Res_Greater_500_Serializer,Restaurant_details_with_count_Serializer,IteamListSerializer,UserSerializer,Cat_resSerializer, RestaurantSerializer,IteamSSerializer,CustomeIteamSSerializer
from rest_framework import viewsets, generics
from django.db.models import Sum



# class Apioverview(GenericAPIView):
#     permission_classes = (IsAuthenticated,)   
#     def get(self, request):
#         api_urls={
#         "For Access Token":"api-token-auth/",
#         'Restaurant List':'res_data/',
#         'Restaurant List By Single ID':'res_data_id/<int:id>',
#         'Category List':'cat_data/',
#         'Category List by single ID':'cat_data_id/<int:id>',
#         'Iteams List':'iteam_data/',
#         'Iteam by Particular ID':'iteam_data_id/<int:id>',

#     }   
#         return Response(api_urls)


# class ResDataWithID(GenericAPIView):
    
#     permission_classes = (IsAuthenticated,)  
#     serializer_class=RestaurantSerializer  
#     def get(self,request,id):
#         res=Restaurant.objects.get(id=id)
#         user_res=UserSerializer(res.owner,many=False)
#         serializer=RestaurantSerializer(res)
#         return Response({"Restaurant":serializer.data,"Owner":user_res.data})
     
#     def put(self,request,id):
#             res=Restaurant.objects.get(id=id)
#             serializer=RestaurantSerializer(res,data=request.data,partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Data Updated'})
#             return(serializer.errors)
      
#     def delete(self,request,id):
#             res=Restaurant.objects.get(id=id)
#             res.delete()
#             return Response({'msg':'Data Deleted'})

# class RestData(GenericAPIView):
#     serializer_class=RestaurantSerializer
#     permission_classes = (IsAuthenticated,)    
#     def get(self,request):
#         res=Restaurant.objects.all()
#         serializer=RestaurantSerializer(res,many=True)
#         return Response(serializer.data)
          
#     def post(self,request):
#         serializer=RestaurantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Inserted'})
#         return(serializer.errors)
    
# class CatData(GenericAPIView):
#     serializer_class=Cat_resSerializer
#     permission_classes = (IsAuthenticated,)    
#     def get(self,request):
#         cat=Cat_Res.objects.all()
#         serializer=Cat_resSerializer(cat,many=True)
#         return Response(serializer.data)
     
#     def post(self,request):    
#         serializer=Cat_resSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Inserted'})
#         return(serializer.errors)

# class CatDataWithId(GenericAPIView):
#     serializer_class=Cat_resSerializer
#     permission_classes = (IsAuthenticated,)    
#     def get(self,request,id):
#         cat=Cat_Res.objects.get(id=id)
#         serializer=Cat_resSerializer(cat)
#         res=RestaurantSerializer(cat.res,many=False)
#         return Response({'category':serializer.data,'Restaurant':res.data})
       
#     def put(self,request,id):
#         cat=Cat_Res.objects.get(id=id)
#         serializer=Cat_resSerializer(cat,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return(serializer.errors)
       
#     def delete(self,request,id):
#         cat=Cat_Res.objects.get(id=id)
#         cat.delete()
#         return Response({'msg':'Data Deleted'})

# class IteamData(GenericAPIView):
#     serializer_class=IteamSSerializer
#     permission_classes = (IsAuthenticated,)    
#     def get(self,request):
#         iteam=Iteams.objects.all()
#         serializer=IteamSSerializer(iteam,many=True)
#         return Response(serializer.data)
       
#     def post(self,request):
#         serializer=IteamSSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Inserted'})
#         return(serializer.errors)

# class IteamWithID(GenericAPIView):
#     permission_classes = (IsAuthenticated,)    
#     def get(self,request,id):
#         iteam=Iteams.objects.get(id=id)
#         user_res=UserSerializer(iteam.cat.res.owner,many=False)
#         res=RestaurantSerializer(iteam.cat.res,many=False)
#         cat = Cat_resSerializer(iteam.cat,many=False)
#         serializer=IteamSSerializer(iteam)
#         return Response({'item':serializer.data,'category':cat.data,'restaurant':res.data,"Owner":user_res.data})
    
#     def put(self,request,id):
#         iteam=Iteams.objects.get(id=id)
#         serializer=IteamSSerializer(iteam,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return(serializer.errors)
       
#     def delete(self,request,id):
#         iteam=Iteams.objects.get(id=id)
#         iteam.delete()
#         return Response({'msg':'Data Deleted'})

# # class listOfResWhichContIteam(GenericAPIView):
# #     #permission_classes = (IsAuthenticated,)
# #     def get(self,request):

# #         queryset = Iteams.objects.all()
# #         serializer_class = CustomeIteamSSerializer()
# #         return Response(json.dumps(serializer_class))
        
    


       

# #   1.view all item with all details like restaurant and category

# class All_Items_with_res_cat(GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self,request):
#         queryset = Iteams.objects.all()
#         serializer_class=IteamListSerializer(queryset,many=True)
#         return Response(serializer_class.data)
    
    
#     # def get(self,request,id):
#     #     queryset = Iteams.objects.get(iteam_id=id)
#     #     serializer_class=IteamListSerializer(queryset,many=False)
#     #     return Response(serializer_class.data)

# #   2.list of restaurant which contain item 
# class RestaurantList(GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self,request):
#         queryset = Iteams.objects.all()
#         serializer_class =CustomeIteamSSerializer(queryset,many=True)
#         return Response(serializer_class.data)



# #   3.list of categories with all item detail using restaurant id
# class all_iteam_wich_cat_using_res(GenericAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self,request,id):
#         queryset=Iteams.objects.filter(restaurant_id=id)
#         serializer_class=all_iteam_with_cat_using_res_Serializer(queryset,many=True)
#         return Response(serializer_class.data)


# #   4. return restaurant details with item count (Number of item associate with restaurant)
# class Restaurant_details_with_count(GenericAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self,request,id):
#         queryset=Restaurant.objects.get(id=id)
#         serializer_classes=Restaurant_details_with_count_Serializer(queryset,many=False)
#         return Response(serializer_classes.data)

# #   5.view all items order by price
# class Iteam_order_by_price(GenericAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self,request):
#         queryset=Iteams.objects.all().order_by('price')
#         serializer_class =IteamSSerializer(queryset,many=True)
#         return Response(serializer_class.data)


# #   6. return all restaurant which has item total greater than 50 Rs
# class Res_Greater_500(GenericAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self,request):
#         queryset=Restaurant.objects.all()
#         grt_50_list=[]
#         for i in queryset:
#             iteam_price=Iteams.objects.filter(restaurant_id=i.id).aggregate(total_price=Sum('price'))
#             if iteam_price['total_price'] is not None:
#                 if iteam_price['total_price'] > 500:
#                     grt_50_list.append(i)
#                 else:
#                     pass
#             else:
#                 pass
        
#         serializer_class=Res_Greater_500_Serializer(grt_50_list,many=True)
#         return Response(serializer_class.data)
            



#-------------------------------write your code here-----------------------------------
