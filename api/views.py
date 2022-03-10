from urllib import response
from rest_framework.generics import GenericAPIView
from .models import Restaurant,Cat_Res,Iteams
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from django.db.models import Sum
from .serializers import IteamsDataSerializer
from rest_framework.views import APIView

class IteamsData(APIView):
    def get(self,request):
        iteam=Iteams.objects.all()
        serializer=IteamsDataSerializer(iteam,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=IteamsDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted'})
        return(serializer.errors)

