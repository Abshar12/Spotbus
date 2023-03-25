from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 100)



class Route(models.Model):
    registered_arrival_time = models.CharField(max_length=50)

class Bus(models.Model):
    schedule_start_time = models.CharField(max_length=50)
    

class Address(models.Model):
    entity = models.CharField(max_length=100)
    apt_plot =  models.CharField(max_length=100)
    street =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    state =  models.CharField(max_length=100)
    zip_code =  models.CharField(max_length=8)
    route = models.ForeignKey(Route,on_delete=models.CASCADE,default = None)

class GeoLocation(models.Model):
    latitude =  models.CharField(max_length=100)
    longitude =  models.CharField(max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,default = None)

