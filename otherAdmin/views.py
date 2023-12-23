from django.shortcuts import render
from .models import *
from .serializers import *
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, 
                    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class StateListViews(ListAPIView):
    queryset = OtherData.objects.all().order_by('State').distinct()
    serializer_class = OtherStateSerializer
    permission_classes = [AllowAny]  
    filter_backends = [OrderingFilter]
    # ordering_fields = ['State']
    
# class CityListViews(viewsets.ModelViewSet):
class CityListViews(ListAPIView):
    queryset = OtherData.objects.all()
    serializer_class = OtherCitySerializer
    permission_classes = [AllowAny]  
    # filter_backends = [OrderingFilter]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['State']
    ordering_fields = ['City']

class OtherTypeListViews(ListAPIView):
    queryset = OtherData.objects.all()
    serializer_class = OtherTypeSerializer
    permission_classes = [AllowAny]  
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['Type']
    filterset_fields = ['State', 'City'] #City isme jo data aayega use case insensitive banana hai

# OtherData Views
class OtherDataViewSet(viewsets.ModelViewSet):
    queryset = OtherData.objects.all()
    serializer_class = OtherDataSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['State', 'District', 'Type'] #City isme jo data aayega use case insensitive banana hai

# Live Section Start
class Today_Live_StatusViewSet(viewsets.ModelViewSet):
    queryset = Today_Live_Status.objects.all()
    serializer_class = Today_Live_StatusSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'otherdata'

class Current_Live_StatusViewSet(viewsets.ModelViewSet):
    queryset = Current_Live_Status.objects.all()
    serializer_class = Current_Live_StatusSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'otherdata'

class Collected_Live_PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Collected_Live_Prescription.objects.all()
    serializer_class = Collected_Live_PrescriptionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'otherdata'

class Running_Live_PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Running_Live_Prescription.objects.all()
    serializer_class = Running_Live_PrescriptionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'otherdata'
# Live Section End

# Checkups Data
class CheckupViewSet(viewsets.ModelViewSet):
    queryset = Checkup.objects.all()
    serializer_class = CheckupSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['otherdata']
    # lookup_field = 'DIN'

# Facility Views
class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['otherdata']

# Employ Views
class EmployViewSet(viewsets.ModelViewSet):
    queryset = Employ.objects.all().order_by('Position')
    serializer_class = EmploySerializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['otherdata']

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = Images_Serializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['otherdata']

class Complain_suggessionViewSet(viewsets.ModelViewSet):
    queryset = Complain_suggession.objects.all()
    serializer_class = Complain_suggessionSerializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['otherdata']

class Other_NotificationViewSet(viewsets.ModelViewSet):
    queryset = Other_Notification.objects.all()
    serializer_class = Other_NotificationSerializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['otherdata']


