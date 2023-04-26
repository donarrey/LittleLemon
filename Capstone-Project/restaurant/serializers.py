#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuIterm

class MenuItemSerializer(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

#class BookingSerializer(serializers.ModelSerializers):
    
    