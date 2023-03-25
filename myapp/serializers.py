from rest_framework import serializers
from myapp.models import *



class RouteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Route
        fields = ['registered_arrival_time']


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = "__all__"

class GeolocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GeoLocation
        fields = "__all__"

class GetAddressSerializer(serializers.ModelSerializer):
    route = RouteSerializer()
    class Meta:
        model = Address
        fields = "__all__"



class GetDataSerializer(serializers.ModelSerializer):
    address = GetAddressSerializer()
    class Meta:
        model = GeoLocation
        fields = "__all__"
    