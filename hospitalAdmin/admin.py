from django.contrib import admin
from .models import (HospitalData, DoctorDetail, Disease, Today_Live_Status, Current_Live_Status, 
Collected_Live_Prescription, Running_Live_Prescription, Achievement, Prescription, 
BookedPrescriptionStatus, Prescribed, Facility, Employ, Image, Complain_suggession, MultyHospitalData, Hos_Notification)

# Register your models here.
# class StateModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
# admin.site.register(State, StateModelAdmin)

# class CityModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
# admin.site.register(City, CityModelAdmin)

# class DoctorsTypeModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
# admin.site.register(DoctorsType, DoctorsTypeModelAdmin)  


admin.site.register(HospitalData)
# class ClinicModelAdmin(admin.ModelAdmin):
#  list_display = ['id', 'Hospital_Name', 'Hospital_Logo', 'Address', 'District', 'Pin_No', 'State', 'Doctor_Image', 'Doctor_Name', 'Doctor_Degree', 'DrType', 'DrDiseaseName', 'Hospital_Id', 'Registration_No', 'License_No', 'Contact_No']

admin.site.register(DoctorDetail)
# class HomeModelAdmin(admin.ModelAdmin):
#  list_display = ['id', 'Today_Status', 'Current_Status', 'Collected_Prescription', 'Running_Prescription', 'Hospital_Time', 'Consultation_Fees', 'Emergency_Fees', 'Seating_Days', 'Seating_Time', 'Lunch_Tmie', 'Operation_Time', 'Bed_Capacity']

admin.site.register(Disease)

admin.site.register(Today_Live_Status)
admin.site.register(Current_Live_Status)
admin.site.register(Collected_Live_Prescription)
admin.site.register(Running_Live_Prescription)

admin.site.register(Achievement)

admin.site.register(Prescription)

admin.site.register(BookedPrescriptionStatus)

admin.site.register(Prescribed)

class FacilityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'FacilityImg', 'FacilityName', 'FacilityDesc')
admin.site.register(Facility, FacilityModelAdmin)



class EmployModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'EmployImg', 'EmployName', 'EmployDesc']
admin.site.register(Employ, EmployModelAdmin)


admin.site.register(Image)

# class ContactusModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'First_Name', 'Last_Name', 'Email_ID', 'Contact_No', 'City', 'State','Subject')
# admin.site.register(Complain_suggession, ContactusModelAdmin)
admin.site.register(Complain_suggession)

admin.site.register(MultyHospitalData)

# # admin.site.register(ContactData)
# # class ContactdataModelAdmin(admin.ModelAdmin):
# #  list_display = ['id', 'First_Name', 'Last_Name', 'Email_ID', 'Contact_No', 'City', 'State','Subject']


class NotificationDataModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Notice')
admin.site.register(Hos_Notification, NotificationDataModelAdmin)
