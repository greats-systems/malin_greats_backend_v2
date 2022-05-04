from rest_framework import serializers
from .models import AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter, Quotation, ManufacturingSignUp, HealthcareSignUp


class AgricultureSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureSignUp
        fields = '__all__'


class RetailSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailSignUp
        fields = '__all__'


class EducationSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSignUp
        fields = '__all__'


class HealthcareSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareSignUp
        fields = '__all__'


class ManufacturingSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturingSignUp
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
