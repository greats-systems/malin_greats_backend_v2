from django.contrib import admin
from .models import AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter, Quotation, ManufacturingSignUp, HealthcareSignUp


@admin.register(AgricultureSignUp)
class AgricultureSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp", "isFree")


@admin.register(RetailSignUp)
class RetailSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp", "isFree")


@admin.register(EducationSignUp)
class EducationSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp", "isFree")


@admin.register(HealthcareSignUp)
class HealthcareSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp", "isFree")


@admin.register(ManufacturingSignUp)
class ManufacturingSignUpAdmin(admin.ModelAdmin):
    search_fields = ("fullName",)
    list_display = ("fullName", "email", "timestamp", "isFree")


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
