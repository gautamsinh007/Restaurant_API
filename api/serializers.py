from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cat_Res,Restaurant,Iteams
from django.contrib.auth.models import User

class IteamsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Iteams
        fields='__all__'