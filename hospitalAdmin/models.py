from django.db.models.signals import post_save, post_delete
# import string
import uuid
from django.utils.text import slugify
# from django.template.defaultfilters import slugify
from django.urls import reverse
from django.dispatch import receiver
    
from django.db import models
import PIL.Image
# from PIL.Image import Image
# from .forms import SignUpForm
# from django.contrib.auth.models import User
from account.models import User
# from django.shortcuts import reverse
# from .utils import get_random_code

# from django.db.models import Q

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

# For Doctor Identification Number
DIN_STATE_CHOICES = (
    ('', 'Select State'),
    ('ANI', 'Andman & Nicobar Islands'),
    ('ANP', 'Andhra Pradesh'),
    ('ARP', 'Arunachal Pradesh'),
    ('ASM', 'Assam'),       
    ('BHR', 'Bihar'),
    ('CHN', 'Chandigarh'),
    ('CHT', 'Chhattisgarh'),
    ('DNH', 'Dadra & Nagr Haveli'),
    ('DMD', 'Daman & Diu'),
    ('DLH', 'Delhi'),
    ('GOA', 'Goa'),
    ('GUJ', 'Gujrat'),
    ('HRN', 'Haryana'),
    ('HMP', 'Himachal Pradesh'),
    ('JMK', 'Jammu & Kashmir'),
    ('JRK', 'Jharkhand'),
    ('KRT', 'Karnataka'),
    ('KRL', 'Kerala'),
    ('LDP', 'Lakshadweep'),
    ('MDP', 'Madhya Pradesh'),
    ('MHR', 'Maharashtra'),
    ('MNP', 'Manipur'),
    ('MGL', 'Meghalaya'),
    ('MZR', 'Mizoram'),
    ('NGL', 'Nagaland'),
    ('ODS', 'Odisha'),
    ('PDC', 'Puducherry'),
    ('PJB', 'Punjab'),
    ('RJS', 'Rajasthan'),
    ('SKM', 'Sikkim'),
    ('TMN', 'Tamil Nadu'),
    ('TLG', 'Telangana'),
    ('TRP', 'Tripura'),
    ('UTK', 'Uttarakhand'),
    ('UTP', 'Uttar Pradesh'),
    ('WSB', 'West Bengal'),
)

DOCTORS_TYPE = (
    ('', 'Doctor\'s Type'),
    ('Dentist', 'Dentist'),
    ('ENT', 'Ear & Nose Throught'),
    ('Gynaecologist', 'Gynaecologist'),
    ('Orthopaedic surgeon', 'Orthopaedic surgeon'),
    ('Paediatrician', 'Paediatrician'),
    ('Psychiatrists', 'Psychiatrists'),
    ('Physician', 'Physician'),
    ('Neurologist', 'Neurologist'),
    ('Cardiologist', 'Cardiologist'),
    ('Radiologist', 'Radiologist'),
    ('Pulmonologist', 'Pulmonologist'),
    ('Endocrinologist', 'Endocrinologist'),
    ('Oncologist', 'Oncologist'),
    ('Cardiothoracic', 'Cardiothoracic'),
    ('Veterinarian', 'Veterinarian'),
)

HOSPITAL_CHOICES = (
    ('', 'Hospital Type'),
    ('Single', 'Single'),
    ('Multy', 'Multy Specilist'),
)

AGE_CHOICES = (
    ('', 'Age Type'),
    ('Year', 'Year'),
    ('Month', 'Month'),
    ('Day', 'Day'),
)

# class State(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class District(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class DoctorsType(models.Model):
#     state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=124)

#     def __str__(self):
#         return self.name

class HospitalData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Hospital_Name = models.CharField(max_length=150)
    Hospital_Logo = models.ImageField(default='hospitalLogo.png', upload_to='hospital_logoimg/', blank=True)
    Hospital_Type = models.CharField(choices=HOSPITAL_CHOICES, max_length=10)
    Address = models.CharField(max_length=150)
    Post = models.CharField(max_length=50)
    Pin_No = models.PositiveIntegerField()
    District = models.CharField(max_length=50)
    State = models.CharField(choices=STATE_CHOICES, max_length=30)
    Bed_Capacity = models.PositiveIntegerField(blank=True, null=True)
    # Vacant_Bed = models.PositiveIntegerField()
    Opening_Days = models.CharField(max_length=50, blank=True)
    Hospital_Timing = models.CharField(max_length=50, blank=True)
    OPD_Timing = models.CharField(max_length=50, blank=True)
    Emergency_Timing = models.CharField(max_length=50, blank=True)
    Registration_No = models.CharField(max_length=25)
    License_No = models.CharField(max_length=30)
    Contact_No = models.PositiveIntegerField()
    # slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 260

        if self.Hospital_Logo:
            pic = PIL.Image.open(self.Hospital_Logo.path)
            pic.thumbnail(SIZE, PIL.Image.LANCZOS)
            pic.save(self.Hospital_Logo.path)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    # def save(self, *args, **kwargs):
    #     to_assign=slugify(self.Hospital_Name)

    #     if HospitalData.objects.filter(Slug=to_assign).exists():
    #         to_assign=to_assign+str(HospitalData.objects.all().count())
        
    #     self.Slug=to_assign
    #     super().save(*args, **kwargs)

    #            'Or'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__initial_Hospital_Name = self.Hospital_Name
    #     self.__initial_Hospital_Type = self.Hospital_Type
            
    # def save(self, *args, **kwargs):
    #     print('******************slug1******************')
    #     ex = False
    #     to_slug = self.slug
    #     if self.Hospital_Name != self.__initial_Hospital_Name or self.Hospital_Type != self.__initial_Hospital_Type or self.slug=="":
    #         if self.Hospital_Name and self.Hospital_Type:
    #             to_slug = slugify(str(self.Hospital_Name) + " " + str(self.Hospital_Type))
    #             ex = HospitalData.objects.filter(slug=to_slug).exists()
    #             while ex:
    #                 to_slug = slugify(to_slug + " " + str(get_random_code()))
    #                 ex = HospitalData.objects.filter(slug=to_slug).exists()
    #         else:
    #             to_slug = str(self.Hospital_Name)
    #     self.slug = to_slug
    #     super().save(*args, **kwargs)


class DoctorDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='doctorDatas')
    
    DIN = models.CharField(max_length=8, unique=True, blank=True)
    State = models.CharField(choices=DIN_STATE_CHOICES, max_length=30)
    
    Image = models.ImageField(default='doctorAvatar.png', upload_to='Doctor_img/')
    Name = models.CharField(max_length=50)
    Type = models.CharField(choices=DOCTORS_TYPE, max_length=30)
    Degree = models.CharField(max_length=200)
    Prescription_Limit = models.PositiveIntegerField()
    Other_Info = models.CharField(max_length=150, null=True, blank=True) #Ex aur kisi city me ya aur kahi par baithte hai etc.
    Consultation_Fees = models.PositiveIntegerField()
    Emergency_Fees = models.PositiveIntegerField(null=True, blank=True)
    Seating_Days = models.CharField(max_length=50)
    Seating_Time = models.CharField(max_length=20)
    Lunch_Tmie = models.CharField(max_length=20)
    Operation_Time = models.CharField(max_length=20, null=True, blank=True)
    # Live Need
    Collected_No_Need = models.BooleanField(default=False)
    Running_No_Need = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True, blank=True, null=True)
    # fees = models.DecimalField(max_digits=2, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 260

        if self.Image:
            pic = Image.open(self.Image.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.Image.path)

    def __str__(self):
        return f"{self.hospitaldata.Hospital_Name}-{self.Name}-{self.Type}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.__initial_Name = self.Name
        # self.__initial_Type = self.Type
        self.__initial_State = self.State
        self.__initial_DIN = self.DIN
    
    # Start DIN    
    def save(self, *args, **kwargs):
        print('***************frist***********************')
        # if self.__initial_DIN is not None :
        if self.__initial_DIN :
            print('********************second************************')
            self.DIN = self.DIN
            return super().save(*args, **kwargs)
        else:
            print('*******************third********************')
            stateCode = self.State
            doctorCount = DoctorDetail.objects.filter(State=self.State).count()
            
            doctorNumber = doctorCount + 1
            if doctorNumber <= 9:
                self.DIN = f'{stateCode}{0}{0}{0}{0}{doctorNumber}'
            elif doctorNumber > 9 and doctorNumber <= 99:
                self.DIN = f'{stateCode}{0}{0}{0}{doctorNumber}'
            elif doctorNumber > 99 and doctorNumber <= 999:
                self.DIN = f'{stateCode}{0}{0}{doctorNumber}'
            elif doctorNumber > 999 and doctorNumber <= 9999:
                self.DIN = f'{stateCode}{0}{doctorNumber}'
            else:
                self.DIN = f'{stateCode}{doctorNumber}'

            DIN = DoctorDetail.objects.filter(DIN=self.DIN).exists()
            if DIN:
                doctorNumber = doctorNumber + 51
                if doctorNumber > 9 and doctorNumber <= 99:
                    self.DIN = f'{stateCode}{0}{0}{0}{doctorNumber}'
                elif doctorNumber > 99 and doctorNumber <= 999:
                    self.DIN = f'{stateCode}{0}{0}{doctorNumber}'
                elif doctorNumber > 999 and doctorNumber <= 9999:
                    self.DIN = f'{stateCode}{0}{doctorNumber}'
                else:
                    self.DIN = f'{stateCode}{doctorNumber}'

            return super().save(*args, **kwargs)
    
    # Slug
    # def save(self, *args, **kwargs):
    #     ex = False
    #     to_slug = self.slug
    #     if self.Name != self.__initial_Name or self.Type != self.__initial_Type or self.slug=="":
    #         if self.Name and self.Type:
    #             to_slug = slugify(str(self.Name) + " " + str(self.Type))
    #             ex = DoctorDetail.objects.filter(slug=to_slug).exists()
    #             while ex:
    #                 to_slug = slugify(to_slug + " " + str(get_random_code()))
    #                 ex = DoctorDetail.objects.filter(slug=to_slug).exists()
    #         else:
    #             to_slug = str(self.Name)
    #     self.slug = to_slug
    #     super().save(*args, **kwargs)

#Other Doctors Name
class OtherDoctorDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='otherdoctordetail')
    Other_Doctor_DIN = models.CharField(max_length=8, unique=True, blank=True)
    Other_Doctor_Name = models.CharField(max_length=50)
    Other_Doctor_Type = models.CharField(choices=DOCTORS_TYPE, max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"{self.doctordetail.Name}-{self.Other_Doctor_Name}"

# Doctor Disease Name
class Disease(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='diseases')
    Disease_Name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.doctordetail.Name}-{self.Disease_Name}"

# Doctor Today Live Status
class Today_Live_Status(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctordetail = models.OneToOneField(DoctorDetail, on_delete=models.CASCADE, related_name='todayDoctorLive')
    # doctordetail = models.OneToOneField(DoctorDetail, on_delete=models.CASCADE, primaryKey=True)
    Today_Status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.doctordetail.Type}"

    @receiver(post_save, sender=DoctorDetail, dispatch_uid='unique_add_Today')
    def add_Today(sender, instance, created, **kwargs):
        DoctorDetail = instance
        if created:
           Today_Live_Status(doctordetail=DoctorDetail).save()

# Doctor Current Live Status
class Current_Live_Status(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctordetail = models.OneToOneField(DoctorDetail, on_delete=models.CASCADE, related_name='currentDoctorLive')
    Current_Status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.doctordetail.Type}"

    @receiver(post_save, sender=DoctorDetail, dispatch_uid='unique_add_current')
    def add_current(sender, instance, created, **kwargs):
        DoctorDetail = instance
        if created:
           Current_Live_Status(doctordetail=DoctorDetail).save()

# Doctor Collected Live Prescription
class Collected_Live_Prescription(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctordetail = models.OneToOneField(DoctorDetail, on_delete=models.CASCADE, related_name='collectedDoctorLive')
    Collected_Prescription = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.doctordetail.Type}"

    @receiver(post_save, sender=DoctorDetail, dispatch_uid='unique_add_collected')
    def add_collected(sender, instance, created, **kwargs):
        DoctorDetail = instance
        if created:
           Collected_Live_Prescription(doctordetail=DoctorDetail).save()

# Doctor Running Live Prescription
class Running_Live_Prescription(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctordetail = models.OneToOneField(DoctorDetail, on_delete=models.CASCADE, related_name='runningDoctorLive')
    Running_Prescription = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.doctordetail.Type}"

    @receiver(post_save, sender=DoctorDetail, dispatch_uid='unique_add_running')
    def add_running(sender, instance, created, **kwargs):
        DoctorDetail = instance
        if created:
           Running_Live_Prescription(doctordetail=DoctorDetail).save()

# Achievement Data
class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='achievements')
    Image = models.ImageField(upload_to='achievementimg/', blank=True)
    Description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.Description}"

# Prescription Data
class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='prescriptions')

    number = models.PositiveSmallIntegerField(default=0)
    DoctorType = models.CharField(max_length=200)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=30)
    Age = models.PositiveIntegerField()
    AgeType = models.CharField(choices=AGE_CHOICES, max_length=5)
    Gender = models.CharField(max_length=10)
    Contact_No = models.PositiveIntegerField()
    Address = models.CharField(max_length=200)
    Post = models.CharField(max_length=50)
    Thana = models.CharField(max_length=50)
    Pin_No = models.PositiveIntegerField()
    City = models.CharField(max_length=50)
    State = models.CharField(choices=STATE_CHOICES, max_length=50)
    TermCondition = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    view_detail = models.BooleanField(default=False)
    prescription_seen = models.BooleanField(default=False)
    Appointment_Date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hospitaldata.Hospital_Name}-{self.doctordetail.Type}-{self.First_Name}-{self.Last_Name}-{self.Appointment_Date}"

    def get_absolute_url(self):
        return reverse('hospitalAdmin:viewHospitalPrescription', args=[str(self.id)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_number = self.number
    
    def save(self, *args, **kwargs):
        if self.__initial_number == 0:
            amount = Prescription.objects.filter(hospitaldata=self.hospitaldata, doctordetail=self.doctordetail, Appointment_Date=self.Appointment_Date).count()
            self.number = amount + 1
            return super().save(*args, **kwargs)
        else:
            self.number = self.__initial_number
            return super().save(*args, **kwargs)

# Booked Prescription Status
class BookedPrescriptionStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='bookedPrescriptions')

    Appointment_Date = models.DateField(null=True)
    Collected_No = models.PositiveIntegerField()
    Booking_Status = models.BooleanField(default=True)
    # created = models.DateTimeField(null=True)
    def __str__(self):
        return f"{self.hospitaldata.Hospital_Name}-{self.doctordetail.Type}-{self.Appointment_Date}-{self.Collected_No}"

# Prescribed Prescription Data
class Prescribed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='prescrbeds')

    number = models.PositiveSmallIntegerField(default=0)
    DoctorType = models.CharField(max_length=200)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=30)
    Age = models.PositiveIntegerField()
    AgeType = models.CharField(choices=AGE_CHOICES, max_length=5)
    Gender = models.CharField(max_length=10)
    Contact_No = models.PositiveIntegerField()
    Address = models.CharField(max_length=200)
    Post = models.CharField(max_length=50)
    Thana = models.CharField(max_length=50)
    Pin_No = models.PositiveIntegerField()
    City = models.CharField(max_length=50)
    State = models.CharField(choices=STATE_CHOICES, max_length=50)
    TermCondition = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    view_detail = models.BooleanField(default=False)
    prescription_seen = models.BooleanField(default=False)
    Appointment_Date = models.DateField(null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    # date = models.DateField()
    # # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField()

    def __str__(self):
        return f"{self.hospitaldata.Hospital_Name}-{self.doctordetail.Type}-{self.First_Name}-{self.Last_Name}"

    def get_absolute_url(self):
        return reverse('hospitalAdmin:viewHospitalPrescribed', args=[str(self.id)])

# Hospital Facility    
class Facility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='facilities')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='facilities')
    FacilityImg = models.ImageField(default='facility.png', upload_to='facilityimg/', blank=True)
    FacilityName = models.CharField(max_length=100)
    FacilityDesc = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.FacilityName}"

    def get_absolute_url(self):
        return reverse('hospitalAdmin:updateHospitalFacility', args=[str(self.id)])

# Hospital Images    
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usr_images')
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(default='facility.png', upload_to='hospitalimg/', blank=True)
    ImageName = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.ImageName}"

# Hospital Employ    
class Employ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='employes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usr_employees')
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='employees')
    EmployImg = models.ImageField(default='avatar.png', upload_to='employimg/')
    EmployName = models.CharField(max_length=100)
    EmployDesc = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.EmployName}"

    def get_absolute_url(self):
        return reverse('hospitalAdmin:updateHospitalEmploy', args=[str(self.id)])
  
#Hospital Complain & Suggessions
class Complain_suggession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='complains')
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='complains')
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
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.First_Name}-{self.Last_Name}"

    def get_absolute_url(self):
        return reverse('hospitalAdmin:viewHospitalAdminCompSuggession', args=[str(self.id)])

#Multy Hospital Data    
class MultyHospitalData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='multy_hospital_data')
    doctordetail = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, related_name='multy_doctor_data')
    DrDIN = models.CharField(max_length=8)
    DrName = models.CharField(max_length=50)
    DrType = models.CharField(choices=DOCTORS_TYPE, max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}-{self.DrDIN}"

# Hospital Notifications
class Hos_Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # hospitaldata = models.ForeignKey(HospitalData, on_delete=models.CASCADE, related_name='hosNotifications')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctordetail = models.OneToOneField(DoctorDetail, on_delete=models.CASCADE, related_name='notifications', null=True)
    Title = models.CharField(max_length=100)
    Notice = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.doctordetail.hospitaldata.Hospital_Name}-{self.doctordetail.Name}"

    def get_absolute_url(self):
        return reverse('hospitalAdmin:edit_hospital_notification', args=[str(self.id)])
