from django.contrib import admin
from .models import DoctorDisease, Contactus, IssueNotification, Aboutus, TermCondition

# Register your models here.  
class DoctorDiseaseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Language', 'Doctor_Type', 'Disease_Name')
admin.site.register(DoctorDisease, DoctorDiseaseModelAdmin)

class ContactusModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'First_Name', 'Last_Name', 'Email_ID', 'Contact_No', 'City', 'State', 'Subject', 'is_seen')
admin.site.register(Contactus, ContactusModelAdmin)

class IssueNotificationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Notification_Type', 'Title', 'Description')
admin.site.register(IssueNotification, IssueNotificationModelAdmin)

class AboutusModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'AboutTitle', 'AboutDescription')
admin.site.register(Aboutus, AboutusModelAdmin)

class TermConditionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'TermCondTitle', 'TermCondDescription')
admin.site.register(TermCondition, TermConditionModelAdmin)