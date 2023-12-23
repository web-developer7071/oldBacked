from .models import DoctorDisease, Contactus, IssueNotification, Aboutus, TermCondition
# from .models import *
from rest_framework import serializers

class DoctorDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDisease
        # fields = ['id', 'Image', 'Name', 'Type', 'Degree', 'DiseaseName', 'Prescription_Limit', 'Consultation_Fees', 'Emergency_Fees', 'Seating_Days', 'Seating_Time', 'Lunch_Tmie', 'Operation_Time']
        fields = '__all__'

class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'

class IssueNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueNotification
        fields = '__all__'

class AboutusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = '__all__'

class TermConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCondition
        fields = '__all__'
