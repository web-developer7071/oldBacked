from django.urls import path, include
# # from django.conf import settings
# # from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
# from frontPage.forms import MyPasswordChangeForm

from .views import *
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = "hospitalAdmin"

# # (hospitalAdminHomeView, hospitalAdminFacilityView, updateHospitalFacilityView, deleteHospitalFacilityView, 
# #                     hospitalAdminEmployView, updateHospitalEmployView, deleteHospitalEmployView, hospitalAdminPrescriptionView, 
# #                     updateHospitalDataView, deleteHospitalDataView, updateDoctorDataView, UpdateUserProfileView, hospitalAdminNotificationView,
# #                     editHospitalNotificationView, deleteHospitalNotificationView, hospitalAdminCompSuggessionView, editHospitalAdminCompSuggessionView, deleteHospitalAdminCompSuggessionView)

# app_name = 'hospitalAdmin'

urlpatterns = [
    path('statelist/', StateListViews.as_view(), name='statelist'),
]
# urlpatterns = [
#     # path('hospitalAdminHome/', hospitalAdminHomeView, name='hospitalAdminHome'),
#     path('updateUserProfile/', UpdateUserProfileView, name='updateUserProfile'),
#     path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='HospitalAdmin/updateProfile_and_password.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
#     path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='HospitalAdmin/passwordchangedone.html'), name='passwordchangedone'),
    
#     path('updateHospitalData/<slug:slug>/', updateHospitalDataView, name='updateHospitalData'),
#     path('deleteHospitalData/<slug:slug>/', deleteHospitalDataView, name='deleteHospitalData'),

#     path('createDoctorData/', createDoctorDataView, name='createDoctorData'),
#     path('update_deleteMultyDoctorData/', update_deleteMultyDoctorDataView, name='update_deleteMultyDoctorData'),
#     path('updateDoctorData/<slug:slug>/', updateDoctorDataView, name='updateDoctorData'),
#     path('deleteDoctorData/<slug:slug>/', deleteDoctorDataView, name='deleteDoctorData'),

#     path('multyHospitalDoctorAdminHome/<slug:slug>/', multyHospitalDoctorAdminHomeView, name='multyHospitalDoctorAdminHome'),
#     path('multyHospitalDoctorAdminPrescription/<slug:slug>/', multyHospitalDoctorAdminPrescriptionView, name='multyHospitalDoctorAdminPrescription'),
#     path('MultyHospitalDoctorAdminNotification/<slug:slug>/', MultyHospitalDoctorAdminNotificationView, name='MultyHospitalDoctorAdminNotification'),

#     path('hospitalAdminFacility/', hospitalAdminFacilityView, name='hospitalAdminFacility'),
#     path('hospitalAdminEmploy/', hospitalAdminEmployView, name='hospitalAdminEmploy'),
#     path('hospitalAdminPrescription/', hospitalAdminPrescriptionView, name='hospitalAdminPrescription'),
#     path('viewHospitalPrescription/<uuid:deta_id>/', viewHospitalPrescriptionView, name='viewHospitalPrescription'),
#     path('editHospitalPrescription/<uuid:deta_id>/', editHospitalPrescriptionView, name='editHospitalPrescription'),
#     path('deleteHospitalPrescription/<uuid:deta_id>/', deleteHospitalPrescriptionView, name='deleteHospitalPrescription'),
    
#     path('hospitalAdminBookedPrescription/', hospitalAdminBookedPrescriptionView, name='hospitalAdminBookedPrescription'),
#     path('hospitalAdminBookedAllPrescription/', hospitalAdminBookedAllPrescriptionView, name='hospitalAdminBookedAllPrescription'),
#     path('multyHospitalDoctorAdminBookedPrescription/<slug:slug>/', multyHospitalDoctorAdminBookedPrescriptionView, name='multyHospitalDoctorAdminBookedPrescription'),
#     path('multyHospitalDoctorAdminBookedAllPrescription/<slug:slug>/', multyHospitalDoctorAdminBookedAllPrescriptionView, name='multyHospitalDoctorAdminBookedAllPrescription'),
    
#     path('hospitalTransferPrescription/', hospitalTransferPrescriptionView, name='hospitalTransferPrescription'),
#     # (?P<dateId>)$
#     path('multyHospitalTransferPrescription/<slug:slug>/', multyHospitalTransferPrescriptionView, name='multyHospitalTransferPrescription'),
    
#     # path('hospitalAdminPrescribed/', hospitalAdminPrescribedView, name='hospitalAdminPrescribed', kwargs={'dateId': ''}),
#     # path('hospitalAdminPrescribed/<dateId>', hospitalAdminPrescribedView, name='hospitalAdminPrescribed'),
#     path('hospitalAdminPrescribed/', hospitalAdminPrescribedView, name='hospitalAdminPrescribed'),
#     path('multyHospitalAdminPrescribed/<slug:slug>/', multyHospitalAdminPrescribedView, name='multyHospitalAdminPrescribed'),
    
#     path('viewHospitalPrescribed/<uuid:deta_id>/', viewHospitalPrescribedView, name='viewHospitalPrescribed'),
#     path('hospitalAdminRestorePrescription/', hospitalAdminRestorePrescriptionView, name='hospitalAdminRestorePrescription'),
#     path('multyHospitalDoctorAdminRestorePrescription/<slug:slug>/', multyHospitalDoctorAdminRestorePrescriptionView, name='multyHospitalDoctorAdminRestorePrescription'),
    
#     path('hospitalAdminNotification/', hospitalAdminNotificationView, name='hospitalAdminNotification'),
#     path('edit_hospital_notification/<uuid:deta_id>/', editHospitalNotificationView, name='edit_hospital_notification'),
#     path('delete_hospital_notification/<uuid:deta_id>/', deleteHospitalNotificationView, name='delete_hospital_notification'),   

#     path('hospitalAdminCompSuggession/', hospitalAdminCompSuggessionView, name='hospitalAdminCompSuggession'),
#     path('viewHospitalAdminCompSuggession/<uuid:deta_id>/', viewHospitalAdminCompSuggessionView, name='viewHospitalAdminCompSuggession'),
#     path('deleteHospitalAdminCompSuggession/<uuid:deta_id>/', deleteHospitalAdminCompSuggessionView, name='deleteHospitalAdminCompSuggession'),
    
#     path('updateHospitalFacility/<uuid:deta_id>/', updateHospitalFacilityView, name='updateHospitalFacility'),
#     path('deleteHospitalFacility/<uuid:deta_id>/', deleteHospitalFacilityView, name='deleteHospitalFacility'),

#     path('updateHospitalEmploy/<uuid:deta_id>/', updateHospitalEmployView, name='updateHospitalEmploy'),
#     path('deleteHospitalEmploy/<uuid:deta_id>/', deleteHospitalEmployView, name='deleteHospitalEmploy'),
    
# ]