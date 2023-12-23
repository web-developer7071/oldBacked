from django.db import models
import uuid
# from django.template.defaultfilters import slugify
# from django.utils.text import slugify
from django.urls import reverse
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

LANGUAGE_CHOICES = [
 ('', 'Select Language'),
 ('English', 'English'),
 ('Hindi', 'Hindi'),
 ('Gujrati', 'Gujrati'),
 ('Punjabi', 'Punjabi'),
 ('Rajsthani', 'Rajsthani'),
 ('Marathi', 'Marathi'),
 ('Bengali', 'Bengali'),
 ('Kashmari', 'Kashmari'),
 ('Malyalam', 'Malyalam'),
 ('Tamil', 'Tamil'),
 ('Telgu', 'Telgu'),
]

USER_TYPE = [
 ('', 'Select User Type'),
 ('Doctor', 'Doctor'),
 ('Other', 'Other'),
 ('Employee', 'Employee'),
]

class User(AbstractUser):
    # First_name = models.CharField(max_length=30)
    # Last_name = models.CharField(max_length=30)
    # Username = models.CharField(max_length=30, unique=True)
    # Password = models.CharField(max_length=30)
    # Password_confirm = models.CharField(max_length=30)
    # Email = models.EmailField(max_length=50, unique=True)

    # User and User Service Type
    user_type = models.CharField(choices=USER_TYPE, max_length=8 , blank=True, null=True )
    admin_user = models.CharField(max_length=30, blank=True, null=True )
    admin_service_type = models.CharField(max_length=15, blank=True, null=True )
    term_cond = models.BooleanField(default=True)

    # Live Need
    Today_Status = models.BooleanField(default=True)
    Current_Status = models.BooleanField(default=True)
    Collected_No = models.BooleanField(default=True)
    Running_No = models.BooleanField(default=True)

    # last_login_time = models.DateTimeField(null=True, blank=True)
    # last_logout_time = models.DateTimeField(null=True, blank=True)

    # USERNAME_FIELD = "Username"

# When change Username from username to Email
    # username = None
    # USERNAME_FIELD = 'Email'

    # REQUIRED_FIELDS = []

class MobileNo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Mobile_No = models.PositiveIntegerField()
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('edit_mobileno', args=[str(self.id)])