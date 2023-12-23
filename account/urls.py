from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoadUserView

# Creating router objects

urlpatterns = [
    # path('user/', UserViewSet.as_view(), name='user'),
    # path('signup/', SignupView.as_view(), name='signup'),
    path('userdata/', LoadUserView.as_view(), name='userdata'),
]