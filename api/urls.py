from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('agric-signup', views.AgricSignUpEmail, name='agric-signup'),
    path('retail-signup', views.RetailSignUpEmail, name='retail-signup'),
    path('edu-signup', views.EduSignUpEmail, name='edu-signup'),
    path('healthcare-signup', views.HealthcareSignUpEmail,
         name='healthcare-signup'),
    path('manufacturing-signup', views.ManufacturingSignUpEmail,
         name='manufacturing-signup'),

    path('contact-email', views.ContactEmail, name='contact-email'),
    path('enquiry-email', views.EnquiryEmail, name='enquiry-email'),
    path('newsletter', views.Newsletter, name='newsletter'),
    path('quotation', views.Quotation, name='quotation'),
]
