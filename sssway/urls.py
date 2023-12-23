"""sssway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# from account import views as accouViews
from account import views as accouViews
from siteAdmin import views
from hospitalAdmin import views as hosViews
from otherAdmin import views as otherViews
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating router objects
router = DefaultRouter()
# Register viewset with router

# Start Site Related Url
# router.register('statelist', views.StateListViews, basename='statlist')
# router.register('citylist', views.CityListViews, basename='citylist')
router.register('user', accouViews.UserViewSet, basename='user')
router.register('doctordisease', views.DoctorDiseaseViewSet, basename='doctordisease')
router.register('contactus', views.ContactusViewSet, basename='contactus')
router.register('issuenotification', views.IssueNotificationViewSet, basename='issuenotification')
router.register('aboutus', views.AboutusViewSet, basename='aboutus')
router.register('termcondition', views.TermConditionViewSet, basename='termcondition')
# end Site Related Url

# Start Hospital Related Url
router.register('hospitaldata', hosViews.HospitalDataViewSet, basename='hospitaldata')
router.register('doctordetail', hosViews.DoctorDetailViewSet, basename='doctordetail')
router.register('diseasenames', hosViews.DiseaseViewSet, basename='diseasenames')

router.register('todaylivestatus', hosViews.Today_Live_StatusViewSet, basename='todaylivestatus')
router.register('currentlivestatus', hosViews.Current_Live_StatusViewSet, basename='currentlivestatus')
router.register('collectedliveprescription', hosViews.Collected_Live_PrescriptionViewSet, basename='collectedliveprescription')
router.register('runningliveprescription', hosViews.Running_Live_PrescriptionViewSet, basename='runningliveprescription')

router.register('achievement', hosViews.AchievementViewSet, basename='achievement')
router.register('facility', hosViews.FacilityViewSet, basename='facility')
router.register('employ', hosViews.EmployViewSet, basename='employ')
router.register('image', hosViews.ImageViewSet, basename='image')
router.register('complainsuggession', hosViews.Complain_suggessionViewSet, basename='complainsuggession')
router.register('multyhospitaldata', hosViews.MultyHospitalDataViewSet, basename='multyhospitaldata')
router.register('hosnotification', hosViews.Hos_NotificationViewSet, basename='hosnotification')
# End Hospital Related Url

# Start Other Related Url
router.register('otherdata', otherViews.OtherDataViewSet, basename='otherdata')

router.register('othertodaylivestatus', otherViews.Today_Live_StatusViewSet, basename='othertodaylivestatus')
router.register('othercurrentlivestatus', otherViews.Current_Live_StatusViewSet, basename='othercurrentlivestatus')
router.register('othercollectedliveprescription', otherViews.Collected_Live_PrescriptionViewSet, basename='othercollectedliveprescription')
router.register('otherrunningliveprescription', otherViews.Running_Live_PrescriptionViewSet, basename='otherrunningliveprescription')

router.register('othercheckup', otherViews.CheckupViewSet, basename='othercheckup')
router.register('otherfacility', otherViews.FacilityViewSet, basename='otherfacility')
router.register('otheremploy', otherViews.EmployViewSet, basename='otheremploy')
router.register('otherimage', otherViews.ImageViewSet, basename='otherimage')
router.register('othercomplainsuggession', otherViews.Complain_suggessionViewSet, basename='othercomplainsuggession')
router.register('otherhosnotification', otherViews.Other_NotificationViewSet, basename='otherhosnotification')
# End Other Related Url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('statelist/', hosViews.StateListViews.as_view(), name='statelist'),
    path('districtlist/', hosViews.DistrictListViews.as_view(), name='districtlist'),
    path('drtypelist/', hosViews.DrTypeListViews.as_view(), name='drtypelist'),
    path('onedoctordata/<str:DIN>/', hosViews.OneDoctorDetailViewSet.as_view(), name='onedoctordata'),
    # path('', include('otherAdmin.urls')),
    path('otherstatelist/', otherViews.StateListViews.as_view(), name='otherstatelist'),
    path('othercitylist/', otherViews.CityListViews.as_view(), name='othercitylist'),
    path('othertypelist/', otherViews.OtherTypeListViews.as_view(), name='othertypelist'),
    # path('hospitalAdmin/', include('hospitalAdmin.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'), #token_obtain_pair
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'), #token_refresh
    path('verifytoken/', TokenVerifyView.as_view(), name='verifytoken'), #token_verify
    path('account/', include('account.urls')),
    # path('', include('siteAdmin.urls')),
    # path('hospitalAdmin/', include('hospitalAdmin.urls', namespace='hospitalAdmin')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin UI Management
admin.site.site_header = 'SiraWay Administration'
admin.site.index_title = 'Manage the SiraWay Site'