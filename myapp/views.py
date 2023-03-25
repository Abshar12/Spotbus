from django.shortcuts import render
from myapp.serializers import *
from myapp.models import *
from rest_framework import status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

'''
Adding Address 
'''
class AddAddress(APIView):

    def post(self,request):
        address = AddressSerializer(data=request.data)
        if address.is_valid():
            address.save()
            return Response("Address added successfully",status=status.HTTP_200_OK)
        return Response("Some error occured.",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        address = Address.objects.all()
        serializer = AddressSerializer(address,many=True)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        if Address.objects.filter(id=id).exists():
            address = Address.objects.get(pk=id)
            serializer = AddAddress(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Details updated successfully",status=status.HTTP_200_OK)
        return Response("Address not found", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        
        if Address.objects.filter(id=id).exists():
            address = Address.objects.get(id=id)
            address.delete()
            return Response("Address deleted successfully",status=status.HTTP_200_OK)
        
        return Response("Address not found",status=status.HTTP_400_BAD_REQUEST)
    


'''
Geolocation API
'''

class AddGeolocation(APIView):
    def post(self,request):
        geolocation = GeolocationSerializer(data=request.data)
        if geolocation.is_valid():
            geolocation.save()
            return Response("Geolocation added successfully",status=status.HTTP_200_OK)
        return Response("Some error occured.",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def get(self,request):
        geolocation = GeoLocation.objects.all()
        serializer = GeolocationSerializer(geolocation,many=True)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        if GeoLocation.objects.filter(id=id).exists():
            geolocation = GeoLocation.objects.get(pk=id)
            serializer = GeolocationSerializer(geolocation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Details updated successfully",status=status.HTTP_200_OK)
        return Response("Geolocation not found", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        
        if GeoLocation.objects.filter(id=id).exists():
            geolocation = GeoLocation.objects.get(id=id)
            geolocation.delete()
            return Response("Geolocation deleted successfully",status=status.HTTP_200_OK)
        
        return Response("Geolocation not found",status=status.HTTP_400_BAD_REQUEST) 


'''
Routes API
'''

class AddRoutes(APIView):

    def post(self,request):
        route = RouteSerializer(data=request.data)
        
        if route.is_valid():
            route.save()
            return Response("Route added successfully",status=status.HTTP_200_OK)
        return Response("Some error occured.",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        route = Route.objects.all()
        serializer = RouteSerializer(route,many=True)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        if Route.objects.filter(id=id).exists():
            route = Route.objects.get(pk=id)
            serializer = RouteSerializer(route, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Details updated successfully",status=status.HTTP_200_OK)
        return Response("Route not found", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        
        if Route.objects.filter(id=id).exists():
            route = Route.objects.get(id=id)
            route.delete()
            return Response("Route deleted successfully",status=status.HTTP_200_OK)
        
        return Response("Route not found",status=status.HTTP_400_BAD_REQUEST)


class GetData(APIView):
    def get(self,request):
        route = GeoLocation.objects.all()
        serializer = GetDataSerializer(route,many=True)
        return Response (serializer.data)