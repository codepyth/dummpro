from typing import Any
from django.db import models
from django.contrib.auth.models import User

# class Attachment(models.Model):
#     attachment1 = models.FileField(upload_to='attachments/', null=True, blank=True)
#     attachment2 = models.FileField(upload_to='attachments/', null=True, blank=True)
#     attachment3 = models.FileField(upload_to='attachments/', null=True, blank=True)
#     attachment4 = models.FileField(upload_to='attachments/', null=True, blank=True)

    # def __str__(self):
    #     return f"Attachment {self.id}"

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=90, null=False, blank=False,help_text="member name")
    email = models.EmailField()

    # Personal Information
    OCCUPATION_CHOICES = [
        ('Job', 'Job'),
        ('Business', 'Business'),
        ('Student', 'Student'),
        ('Housewife', 'Housewife'),
        ('Others', 'Others'),
    ]
    GENDER =  [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    relationship = models.CharField(max_length=34, null=True, blank=True)
    dob = models.CharField(max_length=44, null=True, blank=True)
    gender = models.CharField(max_length=40, choices=GENDER, default='Male')
    school_name = models.CharField(max_length=90, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    job_name = models.CharField(max_length=50, null=True, blank=True)
    job_details = models.TextField(null=True, blank=True)
    job_company = models.CharField(max_length=60, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    company_details = models.CharField(max_length=50, null=True, blank=True)
    business_type = models.CharField(max_length=50, null=True, blank=True)
    buisness_details = models.TextField(max_length=800, null=True, blank=True)
    occupation = models.CharField(max_length=10, choices=OCCUPATION_CHOICES, blank=False)
    passport_picture = models.ImageField(upload_to='passport_pictures/', null=True, blank=True)
    occupation_details = models.TextField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    # Passport Information
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    passport_expiry = models.CharField(max_length=33, null=True, blank=True)
    applied_for_edit = models.BooleanField(default=False, null=True, blank=True)

    # Proof of Pakistan Origin
    PROOF_CHOICES = [
        ('NIC', 'NIC'),
        ('POC', 'POC'),
        ('Other', 'Other'),
    ]
    proof_of_origin = models.CharField(max_length=10, choices=PROOF_CHOICES, null=True, blank=True)
    origin_id_number = models.CharField(max_length=20, null=True, blank=True)
    visa_gonna_expire_in_30_days = models.BooleanField(default=False, null=True, blank=True)
    passport_gonna_expire_in_30_days = models.BooleanField(default=False, null=True, blank=True)
    visa_expired = models.BooleanField(default=False, null=True, blank=True)
    passport_expiry = models.BooleanField(default=False, null=True, blank=True)
    # Visa Information
    VISA_CHOICES = [
        ('Permit', 'Permit'),
        ('Visit_Visa', 'Visit Visa'),
        ('Temporary_Permit', 'Temporary Permit'),
        ('Other', 'Other'),
    ]
    visa_document = models.FileField(upload_to='visa_doc/', null=True, blank=True)
    visa_status = models.CharField(max_length=20, choices=VISA_CHOICES, null=True, blank=True)
    visa_expiry_date = models.CharField(max_length=43, null=True, blank=True)
    staying_in_rwanda_since = models.CharField(max_length=33, null=True, blank=True)
    living_with_dependents = models.BooleanField(default=False)

    # Contact Information
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    address_in_rwanda = models.CharField(max_length=50,null=True, blank=True)
    province =  models.CharField(max_length=40,null=True, blank=True)
    district = models.CharField(max_length=40,null=True, blank=True)
    sector = models.CharField(max_length=40,null=True, blank=True)
    cell = models.CharField(max_length=40,null=True,blank=True)

    # Emergency Contact Information
    emergency_country = models.CharField(max_length=50, null=True, blank=True)
    emergency_mobile_number = models.CharField(max_length=20, null=True, blank=True)
    other_full_address = models.CharField(max_length=60,null=True, blank=True)
    contact_name = models.CharField(max_length=50,null=True,blank=True)
    relation = models.CharField(max_length=40,null=True, blank=True)

    attachment1 = models.FileField(upload_to='attachments/', null=True, blank=True)
    attachment2 = models.FileField(upload_to='attachments/', null=True, blank=True)
    attachment3 = models.FileField(upload_to='attachments/', null=True, blank=True)
    attachment4 = models.FileField(upload_to='attachments/', null=True, blank=True)

    # Dependent Information
    dependents = models.ManyToManyField('Dependent', blank=True, related_name='dependents_of_registration')

    STATUS_CHOICES = [
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
        ('PENDING', 'PENDING'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"User {self.id}"


class Dependent(models.Model):
    name = models.CharField(max_length=90,null=False,blank=False)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=50)  # You can use a separate model for countries
    occupation_choices = [
        ('Job', 'Job'),
        ('Business', 'Business'),
        ('Student', 'Student'),
        ('Housewife', 'Housewife'),
        ('Others', 'Others'),
    ]
    occupation = models.CharField(max_length=90, choices=occupation_choices)
    company = models.CharField(max_length=40,blank=False,null=False)
    company_job = models.CharField(max_length=40)
    dependent_passport = models.FileField(upload_to='depenedent')
    institute = models.CharField(max_length=40,blank=False,null=False)
    dependent_visa = models.FileField(upload_to='depenedent')
    occupation_details = models.TextField()
    visa_choices = [
        ('Permit', 'Permit'),
        ('Visit Visa', 'Visit Visa'),
        ('Temporary Permit', 'Temporary Permit'),
        ('Other', 'Other'),
    ]
    visa_status = models.CharField(max_length=20, choices=visa_choices)
    visa_expiry_date = models.CharField(max_length=43)
    living_in_rwanda = models.CharField(max_length=20,null=False,blank=False)
    def __str__(self):
        return f"Dependent of User {self.registration.user.username}"



