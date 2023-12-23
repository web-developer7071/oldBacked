from .models import *
from rest_framework import serializers

class OtherStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherData
        fields = ['id', 'State']
        # fields = ['City', 'State']

class OtherCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherData
        fields = ['id', 'City']

class OtherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherData
        fields = ['id', 'Type']

class OtherButtonToday_Live_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today_Live_Status
        fields = ['Today_Status']

class OtherDataSerializer(serializers.ModelSerializer):
    todayLive = OtherButtonToday_Live_StatusSerializer(many=False, read_only=True)
    class Meta:
        model = OtherData
        fields = ['url', 'id', 'user', 'Name', 'Logo', 'Type', 'Address', 'Post', 'Pin_No', 'District', 'State', 'Opening_Days', 'Opening_Time', 'Payment_Mode', 'Registration_No', 'Contact_No_First', 'Contact_No_Second', 'Collected_No_Need', 'Running_No_Need', 'created', 'updated', 'todayLive']

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

class CheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkup
        fields = ['id', 'otherdata', 'Name', 'Fees', 'created', 'updated']

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'otherdata', 'FacilityImage', 'FacilityName', 'FacilityDesc', 'created', 'updated']

class Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        fields = '__all__'

class Complain_suggessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_suggession
        fields = '__all__'

class Other_NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Notification
        fields = '__all__'
