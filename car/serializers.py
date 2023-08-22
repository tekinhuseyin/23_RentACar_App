from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):   
    class Meta:
        model=Car
        fields="__all__"



class ReservationSerializer(serializers.ModelSerializer):
    car=serializers.StringRelatedField()
    car_id=serializers.IntegerField()

    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField()
    # passenger=serializers.StringRelatedField()
    # passenger=serializers.IntegerField()