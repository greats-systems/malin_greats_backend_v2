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

    path('contact-email', views.addContactEmail, name='contact-email'),
    path('enquiry-email', views.addEnquiryEmail, name='enquiry-email'),
    path('newsletter', views.addNewsletter, name='newsletter'),
    path('quotation', views.addQuotation, name='quotation'),

    path('free-domains', views.getFreeDomains, name='free-domains'),
    path('add-agricdomain', views.addAgricultureDomain, name='add-agridomain'),
    path('add-retaildomain', views.addRetailDomain, name='add-retaildomain'),
    path('add-edudomain', views.addEducationDomain,
         name='add-edudomain'),
    path('add-manudomain', views.addManufacturingDomain,
         name='add-manudomain'),
    path('add-healthdomain', views.addHealthcareDomain,
         name='add-healthdomain'),

    path('get-agricsignup', views.getAgriSignUps, name='get-agricsignup'),
    path('get-retailsignup', views.getRetailSignUps, name='get-retailsignup'),
    path('get-edusignup', views.getEduSignUps, name='get-edusignup'),
    path('get-manusignup', views.getManuSignUps, name='get-manusignup'),
    path('get-healthsignup', views.getHealthSignUps, name='get-healthsignup'),

    path('get-agricdomain-specific/<str:pk>',
         views.getAgriDomainSpecific, name='get-agricdomain-specific'),

    path('get-totalsignups',
         views.getTotalSignUps, name='get-totalsignups'),
    #     path('get-totaldomains/<str:pk>',
    #          views.getTotalDomains, name='get-totaldomains'),


    #     path('get-enquiries', views.getEnquiryEmail, name='get-enquiries'),
    path('get-qoutations', views.getAllQuotations, name='get-qoutations'),
    path('get-contacts', views.getAllContacts, name='get-contacts'),
    path('get-enquiries', views.getAllEnquiries, name='get-enquiries'),
    path('get-newsletters', views.getAllNewsletters, name='get-newsletters'),

    path('script', views.TestScript, name='script'),
]
