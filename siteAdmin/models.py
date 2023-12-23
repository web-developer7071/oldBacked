from django.db import models
import uuid
# from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.text import slugify
# from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES = (
    ('', 'Select State'),
    ('Andman & Nicobar Islands', 'Andman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra & Nagr Haveli', 'Dadra & Nagr Haveli'),
    ('Daman & Diu', 'Daman & Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipu'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
)

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

class DoctorDisease(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Language = models.CharField(choices=LANGUAGE_CHOICES, max_length=50)
    Doctor_Type = models.CharField(max_length=30)
    Disease_Name = models.CharField(max_length=200)
    # is_seen = models.BooleanField(default=False)
    # view_detail = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Language}-{self.Doctor_Type}"

    # def get_absolute_url(self):
    #     return reverse('viewContactData', args=[str(self.id)])

class Contactus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=30)
    Email_ID = models.EmailField()
    Contact_No = models.PositiveIntegerField()
    City = models.CharField(max_length=100)
    State = models.CharField(choices=STATE_CHOICES, max_length=50)
    Subject = models.CharField(max_length=200)
    is_seen = models.BooleanField(default=False)
    view_detail = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.First_Name}-{self.Last_Name}-{self.City}-{self.State}"

    def get_absolute_url(self):
        return reverse('viewContactData', args=[str(self.id)])


NOTIFICATION_CHOICES = [
 ('', 'Select Type'),
 ('All', 'All'),
 ('Front Users', 'Front Users'),
 ('Hospitals', 'Hospitals'),
]

class IssueNotification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Notification_Type = models.CharField(choices=NOTIFICATION_CHOICES, max_length=11)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('edit_notification', args=[str(self.id)])

class Aboutus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    AboutTitle = models.CharField(max_length=100)
    AboutDescription = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('edit_about', args=[str(self.id)])

class TermCondition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TermCondTitle = models.CharField(max_length=100)
    TermCondDescription = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('edit_termcond', args=[str(self.id)])

