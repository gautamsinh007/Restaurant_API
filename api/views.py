from urllib import response
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Restaurant,Cat_Res,Iteams
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.db.models import Sum




def home(request):
    return render(request,'api/home.html')