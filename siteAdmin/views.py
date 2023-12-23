from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponsePermanentRedirect
from .models import DoctorDisease, Contactus, IssueNotification, Aboutus, TermCondition
from .serializers import DoctorDiseaseSerializer, ContactusSerializer, IssueNotificationSerializer, AboutusSerializer, TermConditionSerializer
from rest_framework import viewsets
# from django.contrib import messages

# Create your views here.
class DoctorDiseaseViewSet(viewsets.ModelViewSet):
    queryset = DoctorDisease.objects.all()
    serializer_class = DoctorDiseaseSerializer

class ContactusViewSet(viewsets.ReadOnlyModelViewSet):
# class ContactusViewSet(viewsets.ModelViewSet):
    queryset = Contactus.objects.all()
    serializer_class = ContactusSerializer

class IssueNotificationViewSet(viewsets.ModelViewSet):
    queryset = IssueNotification.objects.all()
    serializer_class = IssueNotificationSerializer

class AboutusViewSet(viewsets.ModelViewSet):
    queryset = Aboutus.objects.all()
    serializer_class = AboutusSerializer

class TermConditionViewSet(viewsets.ModelViewSet):
    queryset = TermCondition.objects.all()
    serializer_class = TermConditionSerializer


# def ssswayAdminView(request):
#     if request.user.is_authenticated:
#         if request.user.is_superuser == True:
#             return render(request, 'ssswayAdmin/SuperUserDashboard.html')
#         else:
#             return HttpResponseRedirect('/hospitalAdminHome/')
#     else:
#         return HttpResponseRedirect('/login/')


# # Admin Management
# def adminManagementView(request):
#     if request.user.is_authenticated:
#         if request.user.is_superuser == True:

#             # userData = User.objects.all().filter(id=request.user.id)
#             # context = {
#             #     'userData':userData
#             # }
#             return render(request, 'ssswayAdmin/admin_management.html')
#         else:	
#             return HttpResponseRedirect('/hospitalAdminHome/')
#     else:
#         return HttpResponseRedirect('/login/')


# # Edit Userv Profile 
# def editUserProfileView(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             fm = EditUserProfileForm(request.POST, instance=request.user)
#             if fm.is_valid():
#                 messages.success(request, 'User Profile Updated Successfully!!!')
#                 fm.save()
#                 return HttpResponseRedirect('/admin_management/')
#         else:
#             fm = EditUserProfileForm(instance=request.user)
#         return render(request, 'ssswayAdmin/updatePassword_and_Profile.html', {'name':request.user, 'form1':fm, 'formName':'Update Profile'})
#     else:
#         return HttpResponseRedirect('/login/')


# def signup_page(request):    
#     if request.user.is_authenticated:
#         if request.user.is_superuser == True:
#             if request.method == "POST":
#                 fm = SignUpForm(request.POST)
#                 # fm = SignUpForm(request.POST, instance=request.user)
#                 # users = User.objects.all()
#                 if fm.is_valid():
#                     fm.save()
#                     messages.success(request, 'User Account Created Successfully!!!')
#                     return HttpResponseRedirect('/signup_page/')
#             else:
#                 fm = SignUpForm()
#                 # users = User.objects.all()
#             return render(request, 'SssWayAdmin/sign_up_page.html', {'form':fm})
#             # return render(request, 'enroll/profile.html', {'name':request.user.name, 'form':fm})
#         else:	
#             return HttpResponseRedirect('/hospitalAdminHome/')
#     else:
#         return HttpResponseRedirect('/login/')

