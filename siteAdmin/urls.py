# # from ssswayFrontPage.views import user_login
from django.urls import path
# # from django.conf import settings
# # from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
# from .views import ssswayAdminView, adminManagementView, editUserProfileView, signup_page, issueNotification, editNotification, deleteNotification, contactData, viewContactData, deleteContactData
# #  addPlace, deleteCity, 
# from frontPage.forms import MyPasswordChangeForm
# # from ssswayFrontPage.forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

app_name = "siteAdmin"

# urlpatterns = [
#     # path('ssswayAdminHome/', ssswayAdminView, name='ssswayAdminHome'),
#     path('admin_management/', adminManagementView, name='admin_management'),
#     path('editUserProfile/', editUserProfileView, name='editUserProfile'),
#     path('superUserPasswordchange/', auth_views.PasswordChangeView.as_view(template_name='ssswayAdmin/updatePassword_and_Profile.html', form_class=MyPasswordChangeForm, success_url='/admin_management/'), name='superUserPasswordchange'),
#     # path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='ssswayAdmin/passwordchangedone.html'), name='passwordchangedone'),
    
#     path('signup_page/', signup_page, name='signup_page'),
#     path('issue_notification/', issueNotification, name='issue_notification'),
#     # path('add_place/', addPlace, name='add_place'),
#     # path('delete_city/<int:deta_id>/', deleteCity, name='delete_city'),
#     path('issue_notification/', issueNotification, name='issue_notification'),
#     path('delete_notification/<uuid:deta_id>/', deleteNotification, name='delete_notification'),
#     path('contactData/', contactData, name='contactData'),
#     path('viewContactData/<uuid:deta_id>/', viewContactData, name='viewContactData'),
#     path('deleteContactData/<uuid:deta_id>/', deleteContactData, name='deleteContactData'),
# ]


# ****************************** Front Page URLs **************************

# from .views import *
# from hospitalAdmin.views import hospitalAdminHomeView
# from hospitalAdmin.context_processors import complete_front_data
# from ssswayAdmin.views import ssswayAdminView
# from django.contrib.auth import views as auth_views
# from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
#     # path('ajax_load_cities', loadCities, name='ajax_load_cities'),
#     # path('ajax_load_doctype', loadDoctorTypr, name='ajax_load_doctype'),
#     path('search_data/', search_dataView, name='search_data'),
#     path('hospitalHome/<slug:slug>/', hospitalPageView, name='hospitalHome'),
#     path('hospitalDoctorPage/<slug:slug>/', hospitalDoctorPageView, name='hospitalDoctorPage'),
#     path('hospitalPrescription/<slug:slug>/', hospitalPrescriptionView, name='hospitalPrescription'),
#     path('hospitalBookedPrescription/<slug:slug>/', hospitalBookedPrescriptionView, name='hospitalBookedPrescription'),
#     path('hospitalDetailUpdatePrescriptionForm/<slug:slug>/', hospitalDetailUpdatePrescriptionFormView, name='hospitalDetailUpdatePrescriptionForm'),
#     path('hospitalDetailUpdatePrescription/<slug:slug>/', hospitalDetailUpdatePrescriptionView, name='hospitalDetailUpdatePrescription'),
#     path('hospitalUpdatePrescription/<slug:slug>/', hospitalUpdatePrescriptionView, name='hospitalUpdatePrescription'),
#     path('deleteSession/<slug:slug>/', deleteSessionView, name='deleteSession'),
    
#     path('hospitalFacility/<slug:slug>/', hospitalFacilityView, name='hospitalFacility'),
#     path('hospitalEmploy/<slug:slug>/', hospitalEmployView, name='hospitalEmploy'),
#     path('hospitalCompSuggession/<slug:slug>/', hospitalCompSuggessionView, name='hospitalCompSuggession'),
   
#     # path('hospitalPage/<int:id>/', , name='hospitalPage'),
#     path('about_us/', about_us, name='about_us'),
#     path('contact_us/', contact_us, name='contact_us'),
#     path('disease_and_doctor/', disease_and_doctor, name='disease_and_doctor'), 
#     path('term_and_condition/', term_and_condition, name='term_and_condition'),
#     path('login/', user_login, name='login'),

#     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
#     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'), 
    
#     # path('ssswayAdminHome/', ssswayAdminView, name='ssswayAdminHome'),
#     # path('hospitalAdminHome/', hospitalAdminHomeView, name='hospitalAdminHome'),

#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
#     # path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='HospitalAdmin/updateHome.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
#     # path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='HospitalAdmin/passwordchangedone.html'), name='passwordchangedone'),
]