from django.db import models
from django.utils import timezone
from datetime import datetime


def upload_to(instance, filename):
    return filename.format(filename=filename)


class AgricultureSignUp(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isFree = models.BooleanField(default=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class RetailSignUp(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isFree = models.BooleanField(default=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class EducationSignUp(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isFree = models.BooleanField(default=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


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
