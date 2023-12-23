from .models import *
# from .models import (HospitalData, DoctorDetail, Today_Live_Status, Current_Live_Status, 
# Collected_Live_Prescription, Running_Live_Prescription, Prescription, BookedPrescriptionStatus, 
# Prescribed, Facility, Employ, Complain_suggession, Hos_Notification)
from rest_framework import serializers

class HospitalStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalData
        fields = ['id', 'State']
        # fields = ['District', 'State']

class HospitalCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalData
        fields = ['id', 'District']

class DrTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetail
        fields = ['id', 'Type']

# class HospitalDataSerializer(serializers.ModelSerializer):
#     # doctorDatas = serializers.StringRelatedField(many=True, read_only=True)
#     # doctorDatas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     doctorDatas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='doctordetail-detail')
#     # doctorDatas = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
#     # doctorDatas = serializers.HyperlinkedIdentityField(view_name='doctordetail-detail')
#     class Meta:
#         model = HospitalData
#         fields = ['Hospital_Name', 'Hospital_Logo', 'Hospital_Type', 'Address', 'Post', 'Pin_No', 'City', 'State', 'Bed_Capacity', 'Opening_Days', 'Hospital_Timing', 'OPD_Timing', 'Emergency_Timing', 'Registration_No', 'License_No', 'Contact_No', 'created', 'updated', 'doctorDatas']
#         # fields = '__all__'

# Automatically Add ViewDetail link
# class HospitalDataSerializer(serializers.HyperlinkedModelSerializer):
#     # doctorDatas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='doctordetail-detail')
#     class Meta:
#         model = HospitalData
#         fields = ['url','Hospital_Name', 'Hospital_Logo', 'Hospital_Type', 'Address', 'Post', 'Pin_No', 'City', 'State', 'Bed_Capacity', 'Opening_Days', 'Hospital_Timing', 'OPD_Timing', 'Emergency_Timing', 'Registration_No', 'License_No', 'Contact_No', 'created', 'updated', 'doctorDatas']
class DrButtonToday_Live_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today_Live_Status
        fields = ['Today_Status']

class ForHospitalDoctorDetailSerializer(serializers.ModelSerializer):
    todayLive = DrButtonToday_Live_StatusSerializer(many=False, read_only=True)
    DIN = serializers.CharField(read_only=True)
    class Meta:
        model = DoctorDetail
        fields = ['url', 'id', 'DIN', 'State', 'Image', 'Name', 'Type', 'Degree', 'Prescription_Limit', 'Other_Info', 'Consultation_Fees', 'Emergency_Fees', 'Seating_Days', 'Seating_Time', 'Lunch_Tmie', 'Operation_Time', 'created', 'updated', 'todayLive', 'hospitaldata']
        # fields = '__all__'


# Automatically Add ViewDetail
class HospitalDataSerializer(serializers.ModelSerializer):
    doctorDatas = ForHospitalDoctorDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = HospitalData
        fields = ['id', 'Hospital_Name', 'Hospital_Logo', 'Hospital_Type', 'Address', 'Post', 'Pin_No', 'District', 'State', 'Bed_Capacity', 'Opening_Days', 'Hospital_Timing', 'OPD_Timing', 'Emergency_Timing', 'Registration_No', 'License_No', 'Contact_No', 'created', 'updated', 'doctorDatas']
        # fields = '__all__'

class ForDoctorHospitalDataSerializer(serializers.ModelSerializer):
    # doctorDatas = HospitalDoctorDetailSerializer(many=True, read_only=True)    
    class Meta:
        model = HospitalData
        fields = ['id', 'Hospital_Name', 'Hospital_Logo', 'Hospital_Type', 'Address', 'Post', 'Pin_No', 'District', 'State', 'Bed_Capacity', 'Opening_Days', 'Hospital_Timing', 'OPD_Timing', 'Emergency_Timing', 'Registration_No', 'License_No', 'Contact_No', 'created', 'updated']
        # fields = '__all__'

class DoctorDetailSerializer(serializers.ModelSerializer):
    hospitaldata = ForDoctorHospitalDataSerializer(many=False, read_only=True)
    todayDoctorLive = DrButtonToday_Live_StatusSerializer(many=False, read_only=True)
    DIN = serializers.CharField(read_only=True)
    class Meta:
        model = DoctorDetail
        fields = ['url', 'id', 'DIN', 'State', 'Image', 'Name', 'Type', 'Degree', 'Prescription_Limit', 'Other_Info', 'Consultation_Fees', 'Emergency_Fees', 'Seating_Days', 'Seating_Time', 'Lunch_Tmie', 'Operation_Time', 'Collected_No_Need', 'Running_No_Need', 'created', 'updated', 'hospitaldata', 'todayDoctorLive']
        # fields = '__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'
        # fields = ['url', 'id', 'doctordetail', 'DiseaseName']

class OneDoctorDetailSerializer(serializers.ModelSerializer):
    hospitaldata = ForDoctorHospitalDataSerializer(many=False, read_only=True)
    todayLive = DrButtonToday_Live_StatusSerializer(many=False, read_only=True)
    diseases = DiseaseSerializer(many=True, read_only=True)    
    DIN = serializers.CharField(read_only=True)
    class Meta:
        model = DoctorDetail
        fields = ['url', 'id', 'DIN', 'State', 'Image', 'Name', 'Type', 'Degree', 'Prescription_Limit', 'Other_Info', 'Consultation_Fees', 'Emergency_Fees', 'Seating_Days', 'Seating_Time', 'Lunch_Tmie', 'Operation_Time', 'created', 'updated', 'diseases', 'todayLive', 'hospitaldata']
        # fields = '__all__'

class Today_Live_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today_Live_Status
        fields = '__all__'

class Current_Live_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current_Live_Status
        fields = '__all__'

class Collected_Live_PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collected_Live_Prescription
        fields = '__all__'

class Running_Live_PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running_Live_Prescription
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class BookedPrescriptionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedPrescriptionStatus
        fields = '__all__'

class PrescribedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescribed
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        fields = '__all__'

class Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class MultyHospitalData_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MultyHospitalData
        fields = '__all__'

class Complain_suggessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_suggession
        fields = '__all__'

class Hos_NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hos_Notification
        fields = '__all__'
