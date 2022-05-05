from django.contrib import admin
from .models import AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter, Quotation, ManufacturingSignUp, HealthcareSignUp, AgricultureDomain, RetailDomain, EducationDomain, ManufacturingDomain, HealthcareDomain, TotalDomain,  TotalSignUp


@admin.register(AgricultureDomain)
class AgricultureDomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'isOccupied', "isActive", 'timestamp')


@admin.register(AgricultureSignUp)
class AgricultureSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "domain",
                    "domain", "timestamp", "isActive")


@admin.register(RetailDomain)
class RetailDomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'isOccupied', "isActive", 'timestamp')


@admin.register(RetailSignUp)
class RetailSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "domain", "timestamp", "isActive")


@admin.register(EducationDomain)
class EducationDomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'isOccupied', "isActive", 'timestamp')


@admin.register(EducationSignUp)
class EducationSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "domain", "timestamp", "isActive")


@admin.register(HealthcareDomain)
class HealthcareDomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'isOccupied', "isActive", 'timestamp')


@admin.register(HealthcareSignUp)
class HealthcareSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "domain", "timestamp", "isActive")


@admin.register(ManufacturingDomain)
class ManufacturingDomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'isOccupied', "isActive", 'timestamp')


@admin.register(ManufacturingSignUp)
class ManufacturingSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "domain", "timestamp", "isActive")


@admin.register(TotalDomain)
class TotalDomainAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('agricultureTotal', 'retailTotal', 'educationTotal',
                    'healthcareTotal', 'manufacturingTotal', 'timestamp')


@admin.register(TotalSignUp)
class TotalSignUpAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('agricultureTotal', 'retailTotal', 'educationTotal',
                    'healthcareTotal', 'manufacturingTotal', 'timestamp')


@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "companyName", "email",
                    "phoneNumber", "message", "timestamp")


@admin.register(EnquiryEmail)
class EnquiryEmailAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "timestamp")


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp")
