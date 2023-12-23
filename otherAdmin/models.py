from django.db.models.signals import post_save, post_delete
# import string
import uuid
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
    
from django.db import models
# from PIL import Image
import PIL.Image
from account.models import User
# from django.contrib.auth.models import User

# For State Name
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
    ('Manipur', 'Manipur'),
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

SERVICE_TYPE = (
    ('', 'Services Type'),
    ('CT Scan', 'CT Scan'),
    ('Diagnostic Center', 'Diagnostic Center'),
    ('Digital X-Ray', 'Digital X-Ray'),
    ('MRI', 'MRI'),
    ('Pythology', 'Pythology'),
    ('Ultrasound', 'Ultrasound'),
    ('X-Ray', 'X-Ray'),
)

# OTHER_CHOICES = (
#     ('', 'Hospital Type'),
#     ('Single', 'Single'),
#     ('Multy', 'Multy Specilist'),
# )

# AGE_CHOICES = (
#     ('', 'Age Type'),
#     ('Year', 'Year'),
#     ('Month', 'Month'),
#     ('Day', 'Day'),
# )


class OtherData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150)
    Logo = models.ImageField(default='hospitalLogo.png', upload_to='otherlogo/', blank=True)
    Type = models.CharField(choices=SERVICE_TYPE, max_length=100)
    Address = models.CharField(max_length=150)
    Post = models.CharField(max_length=50)
    Pin_No = models.PositiveIntegerField()
    District = models.CharField(max_length=50)
    State = models.CharField(choices=STATE_CHOICES, max_length=30)
    Opening_Days = models.CharField(max_length=50, blank=True)
    Opening_Time = models.CharField(max_length=50, blank=True)
    Payment_Mode = models.CharField(max_length=100)
    Registration_No = models.CharField(max_length=25)
    Contact_No_First = models.PositiveIntegerField()
    Contact_No_Second = models.PositiveIntegerField()
    # Live Need
    Collected_No_Need = models.BooleanField(default=False)
    Running_No_Need = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 260

        if self.Logo:
            pic = PIL.Image.open(self.Logo.path)
            pic.thumbnail(SIZE, PIL.Image.LANCZOS)
            pic.save(self.Logo.path)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

# class ServiceProvider(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     otherdata = models.ForeignKey(OtherData, on_delete=models.CASCADE, related_name='serviceproviders')
#     Image = models.ImageField(default='avatar.png', upload_to='other_service_providerimg/', blank=True)
#     Name = models.CharField(max_length=50)
#     Degree = models.CharField(max_length=100)
#     Experience = models.CharField(max_length=50)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         SIZE = 250, 260

#         if self.Image:
#             pic = PIL.Image.open(self.Image.path)
#             pic.thumbnail(SIZE, PIL.Image.LANCZOS)
#             pic.save(self.Image.path)

#     def __str__(self):
#         return f"{self.otherdata.Name}-{self.Name}"

# Other Services Today Live Status
class Today_Live_Status(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otherTodayLive')
    otherdata = models.OneToOneField(OtherData, on_delete=models.CASCADE, related_name='todayLive')
    Today_Status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.otherdata.Name}"

    @receiver(post_save, sender=OtherData, dispatch_uid='unique_add_Today')
    def add_Today(sender, instance, created, **kwargs):
        OtherData = instance
        if created:
           Today_Live_Status(otherdata=OtherData).save()

# Other Services Current Live Status
class Current_Live_Status(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otherCurrentLive')
    otherdata = models.OneToOneField(OtherData, on_delete=models.CASCADE, related_name='currentLive')
    Current_Status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.otherdata.Name}"

    @receiver(post_save, sender=OtherData, dispatch_uid='unique_add_current')
    def add_current(sender, instance, created, **kwargs):
        OtherData = instance
        if created:
           Current_Live_Status(otherdata=OtherData).save()

# Other Services Live Prescription
class Collected_Live_Prescription(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otherCollectedLive')
    otherdata = models.OneToOneField(OtherData, on_delete=models.CASCADE, related_name='collectedLive')
    Collected_Prescription = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.otherdata.Name}"

    @receiver(post_save, sender=OtherData, dispatch_uid='unique_add_collected')
    def add_collected(sender, instance, created, **kwargs):
        OtherData = instance
        if created:
           Collected_Live_Prescription(otherdata=OtherData).save()

# Other Services Running Live Prescription
class Running_Live_Prescription(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otherRunningLive')
    otherdata = models.OneToOneField(OtherData, on_delete=models.CASCADE, related_name='runningLive')
    Running_Prescription = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.otherdata.Name}"

    @receiver(post_save, sender=OtherData, dispatch_uid='unique_add_running')
    def add_running(sender, instance, created, **kwargs):
        OtherData = instance
        if created:
           Running_Live_Prescription(otherdata=OtherData).save()

# Other Checkups
class Checkup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otherdata = models.ForeignKey(OtherData, on_delete=models.CASCADE, related_name='checkups')
    Name = models.CharField(max_length=50)
    Fees = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.otherdata.Name}-{self.Name}"

# Other Facility    
class Facility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_facilities')
    otherdata = models.ForeignKey(OtherData, on_delete=models.CASCADE, related_name='facilities')
    FacilityImage = models.ImageField(default='facility.png', upload_to='otherfacilityimg/', blank=True)
    FacilityName = models.CharField(max_length=100)
    FacilityDesc = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.otherdata.Name}-{self.FacilityName}"

    # def __str__(self):
    #     return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.FacilityName}"

# Hospital Images    
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_images')
    otherdata = models.ForeignKey(OtherData, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(upload_to='otherimg/', blank=True)
    ImageName = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.otherdata.Name}-{self.ImageName}"

# Hospital Employ    
class Employ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_employees')
    otherdata = models.ForeignKey(OtherData, on_delete=models.CASCADE, related_name='employees')
    Position = models.PositiveIntegerField(null=True)
    Image = models.ImageField(default='avatar.png', upload_to='other_employimg/', blank=True)
    Name = models.CharField(max_length=100, null=True)
    Designation = models.CharField(max_length=200, null=True)
    Degree = models.CharField(max_length=100, blank=True, null=True)
    Experience = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 260

        if self.Image:
            pic = PIL.Image.open(self.Image.path)
            pic.thumbnail(SIZE, PIL.Image.LANCZOS)
            pic.save(self.Image.path)
    
    def __str__(self):
        return f"{self.otherdata.Name}-{self.Name}"

    # def get_absolute_url(self):
    #     return reverse('hospitalAdmin:updateHospitalEmploy', args=[str(self.id)])
  
# Hospital Complain & Suggessions
class Complain_suggession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    otherdata = models.ForeignKey(OtherData, on_delete=models.CASCADE, related_name='complains')
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=30)
    # Email_ID = models.EmailField()
    Contact_No = models.PositiveIntegerField()
    City = models.CharField(max_length=100)
    State = models.CharField(choices=STATE_CHOICES, max_length=50)
    Subject = models.CharField(max_length=200)
    is_seen = models.BooleanField(default=False)
    view_detail = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.otherdata.Name}-{self.First_Name}-{self.Last_Name}"

# Hospital Notifications
class Other_Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otherdata = models.OneToOneField(OtherData, on_delete=models.CASCADE, related_name='othrNotifications')
    Notice = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.otherdata.Name}-{self.Notice}"
    # def get_absolute_url(self):
    #     return reverse('hospitalAdmin:edit_hospital_notification', args=[str(self.id)])
