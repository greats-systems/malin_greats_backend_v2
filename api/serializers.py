from dataclasses import field
from rest_framework import serializers
from .models import AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter, Quotation, ManufacturingSignUp, HealthcareSignUp, AgricultureDomain, RetailDomain, EducationDomain, ManufacturingDomain, HealthcareDomain, TotalDomain,  TotalSignUp


class AgricultureDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureDomain
        fields = '__all__'


class AgricultureSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureSignUp
        fields = '__all__'


class RetailDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailDomain
        fields = '__all__'


class RetailSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailSignUp
        fields = '__all__'


class EducationDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDomain
        fields = '__all__'


class EducationSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSignUp
        fields = '__all__'


class HealthcareDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareDomain
        fields = '__all__'


class HealthcareSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareSignUp
        fields = '__all__'


class ManufacturingDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturingDomain
        fields = '__all__'


class ManufacturingSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturingSignUp
        fields = '__all__'


class TotalDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalDomain
        fields = '__all__'


class TotalSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalSignUp
        fields = '__all__'


class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = '__all__'


class EnquiryEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryEmail
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'
