from django.shortcuts import render
from .models import *
from .serializers import *
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed
# from .serializers import (HospitalDataSerializer, DoctorDetailSerializer, Today_Live_StatusSerializer, Current_Live_StatusSerializer, 
# Collected_Live_PrescriptionSerializer, Running_Live_PrescriptionSerializer, PrescriptionSerializer, BookedPrescriptionStatusSerializer,  
# PrescribedSerializer, FacilitySerializer, EmploySerializer, Complain_suggessionSerializer, Hos_NotificationSerializer)
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import (HospitalData, DoctorDetail, Today_Live_Status, Current_Live_Status, Collected_Live_Prescription, 
# Running_Live_Prescription, Prescription, BookedPrescriptionStatus, Prescribed, Facility, Employ, Complain_suggession, Hos_Notification)

from rest_framework.authentication import SessionAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, 
                    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class StateListViews(ListAPIView):
    # def list(self, request):
    queryset = HospitalData.objects.all().order_by('State').distinct()
    serializer_class = HospitalStateSerializer    
    # statelist = HospitalData.objects.values('State').order_by('State').distinct()
    # statelist = HospitalData.objects.all()
    # serializer = HospitalStateSerializer(statelist, many=True)  
    filter_backends = [OrderingFilter]
    
class DistrictListViews(ListAPIView):
    queryset = HospitalData.objects.all()
    serializer_class = HospitalCitySerializer    
    # filter_backends = [OrderingFilter]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['State']
    ordering_fields = ['District']

class DrTypeListViews(ListAPIView):
    queryset = DoctorDetail.objects.all()
    serializer_class = DrTypeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['Type']
    filterset_fields = ['hospitaldata__State', 'hospitaldata__District'] #hospitaldata__District isme jo data aayega use case insensitive banana hai


# Create your views here.
class HospitalDataViewSet(viewsets.ModelViewSet):
    queryset = HospitalData.objects.all()
    serializer_class = HospitalDataSerializer 
    # permission_classes = [IsAdminUser]
    # For Override Global Authentication and Permission
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     user = self.request.user
    #     return HospitalData.objects.filter(user=user)


class DoctorDetailViewSet(viewsets.ModelViewSet):
    queryset = DoctorDetail.objects.all()
    # queryset = DoctorDetail.objects.all().order_by['-created']
                            # 'Or'
    # queryset = DoctorDetail.objects.all().order_by['?']
    serializer_class = DoctorDetailSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hospitaldata__State', 'hospitaldata__District', 'Type'] #hospitaldata__City isme jo data aayega use case insensitive banana hai

# For one doctor data search 
#             or
# Search by DIN DoctorDetail
class OneDoctorDetailViewSet(RetrieveAPIView):
    queryset = DoctorDetail.objects.all()
    serializer_class = OneDoctorDetailSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'DIN'

    # serializer=OneDoctorDetailSerializer(doctorData)        
    # return Response(serializer.data,status=status.HTTP_200_OK)

    # filter_backends = [SearchFilter]
    # search_fields = ['hospitaldata__State', 'hospitaldata__City', 'Type']
    # def get_queryset(self):
    #     user = self.request.user
    #     return DoctorDetail.objects.filter(user=user)

# Disease Name
class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctordetail']

# Live Section Start
class Today_Live_StatusViewSet(viewsets.ModelViewSet):
    queryset = Today_Live_Status.objects.all()
    serializer_class = Today_Live_StatusSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'doctordetail'

class Current_Live_StatusViewSet(viewsets.ModelViewSet):
    queryset = Current_Live_Status.objects.all()
    serializer_class = Current_Live_StatusSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'doctordetail'

class Collected_Live_PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Collected_Live_Prescription.objects.all()
    serializer_class = Collected_Live_PrescriptionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'doctordetail'

class Running_Live_PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Running_Live_Prescription.objects.all()
    serializer_class = Running_Live_PrescriptionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'doctordetail'
# Live Section End

# Achievement Section Start
class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctordetail']

# Prescription Section Start
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class BookedPrescriptionStatusViewSet(viewsets.ModelViewSet):
    queryset = BookedPrescriptionStatus.objects.all()
    serializer_class = BookedPrescriptionStatusSerializer

class PrescribedViewSet(viewsets.ModelViewSet):
    queryset = Prescribed.objects.all()
    serializer_class = PrescribedSerializer
# Prescription Section End

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctordetail']

class EmployViewSet(viewsets.ModelViewSet):
    queryset = Employ.objects.all()
    serializer_class = EmploySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctordetail']

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = Images_Serializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctordetail']

class MultyHospitalDataViewSet(viewsets.ModelViewSet):
    queryset = MultyHospitalData.objects.all()
    serializer_class = MultyHospitalData_Serializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctordetail']

class Complain_suggessionViewSet(viewsets.ModelViewSet):
    queryset = Complain_suggession.objects.all()
    serializer_class = Complain_suggessionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly] #This is Only IsAuthenticated rahega
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hospitaldata']

class Hos_NotificationViewSet(viewsets.ModelViewSet):
    queryset = Hos_Notification.objects.all()
    serializer_class = Hos_NotificationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hospitaldata']

