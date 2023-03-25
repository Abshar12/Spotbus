from django.urls import path
from myapp.views import *

urlpatterns = [
    path('address',AddAddress.as_view()),
    path('address/<int:id>',AddAddress.as_view()),
    path('geolocation',AddGeolocation.as_view()),
    path('geolocation/<int:id>',AddGeolocation.as_view()),
    path('route',AddRoutes.as_view()),
    path('route/<int:id>',AddRoutes.as_view()),
    path('getdata',GetData.as_view())
]