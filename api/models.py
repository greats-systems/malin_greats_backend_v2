from operator import mod
from django.db import models
from django.utils import timezone
from datetime import datetime


def upload_to(instance, filename):
    return filename.format(filename=filename)


class AgricultureDomain(models.Model):
    name = models.CharField(max_length=250, blank=True,
                            primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isOccupied = models.BooleanField(default=False, blank=True, null=True)
    isActive = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class AgricultureSignUp(models.Model):
    domain = models.ForeignKey(
        'AgricultureDomain', null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=250, blank=True, null=True)
    account = models.CharField(
        blank=True, null=True, max_length=100, default='Free')
    isActive = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class RetailDomain(models.Model):
    name = models.CharField(max_length=250, blank=True, primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isOccupied = models.BooleanField(default=False, blank=True, null=True)
    isActive = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class RetailSignUp(models.Model):
    domain = models.ForeignKey(
        'RetailDomain', null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    account = models.CharField(
        blank=True, null=True, max_length=100, default='Free')
    isActive = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class EducationDomain(models.Model):
    name = models.CharField(max_length=250, blank=True, primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isOccupied = models.BooleanField(default=False, blank=True, null=True)
    isActive = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class EducationSignUp(models.Model):
    domain = models.ForeignKey(
        'EducationDomain', null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    account = models.CharField(
        blank=True, null=True, max_length=100, default='Free')
    isActive = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class HealthcareDomain(models.Model):
    name = models.CharField(max_length=250, blank=True, primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isOccupied = models.BooleanField(default=False, blank=True, null=True)
    isActive = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class HealthcareSignUp(models.Model):
    domain = models.ForeignKey(
        'HealthcareDomain', null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    account = models.CharField(
        blank=True, null=True, max_length=100, default='Free')
    isActive = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class ManufacturingDomain(models.Model):
    name = models.CharField(max_length=250, blank=True, primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isOccupied = models.BooleanField(default=False, blank=True, null=True)
    isActive = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class ManufacturingSignUp(models.Model):
    domain = models.ForeignKey(
        'ManufacturingDomain', null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    account = models.CharField(
        blank=True, null=True, max_length=100, default='Free')
    isActive = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class TotalSignUp(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    agricultureTotal = models.IntegerField(default=0, null=True, blank=True)
    retailTotal = models.IntegerField(default=0, null=True, blank=True)
    educationTotal = models.IntegerField(default=0, null=True, blank=True)
    manufacturingTotal = models.IntegerField(default=0, null=True, blank=True)
    healthcareTotal = models.IntegerField(default=0, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)


class TotalDomain(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    agricultureTotal = models.IntegerField(default=0, null=True, blank=True)
    retailTotal = models.IntegerField(default=0, null=True, blank=True)
    educationTotal = models.IntegerField(default=0, null=True, blank=True)
    manufacturingTotal = models.IntegerField(default=0, null=True, blank=True)
    healthcareTotal = models.IntegerField(default=0, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)


class ContactEmail(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    companyName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phoneNumber = models.CharField(max_length=250, blank=True, null=True)
    # phoneNumber = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class EnquiryEmail(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class Newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.email


class Quotation(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName
