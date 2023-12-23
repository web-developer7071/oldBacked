from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(OtherData)
# class ClinicModelAdmin(admin.ModelAdmin):
#  list_display = ['id', 'Name', 'Logo', 'Type', 'Address', 'District', 'Pin_No', 'State', 'Registration_No', 'Contact_No']

admin.site.register(Today_Live_Status)
admin.site.register(Current_Live_Status)
admin.site.register(Collected_Live_Prescription)
admin.site.register(Running_Live_Prescription)

admin.site.register(Checkup)

admin.site.register(Facility)

admin.site.register(Employ)

admin.site.register(Image)

admin.site.register(Complain_suggession)

class NotificationDataModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'otherdata', 'Notice')
admin.site.register(Other_Notification, NotificationDataModelAdmin)
