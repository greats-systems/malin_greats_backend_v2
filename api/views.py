from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.mail import send_mail
import datetime


from .serializers import AgricultureSignUpSerializer, RetailSignUpSerializer, EducationSignUpSerializer, ContactEmailSerializer, EnquiryEmailSerializer, NewsletterSerializer, QuotationSerializer
from .models import AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter, Quotation


@api_view(['POST'])
def AgricSignUpEmail(request):
    serializer = AgricultureSignUpSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = fullName + 'New Sign Up \n\t Agriculture \n\n ' + fullName + '\n' + email
    if serializer.is_valid():
        send_mail('SmartFarma SignUp HURRY', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def RetailSignUpEmail(request):
    serializer = RetailSignUpSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = 'New Sign Up \n Retail \n\n ' + fullName + '\n' + email
    if serializer.is_valid():
        send_mail('SmartFarma SignUp HURRY', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def EduSignUpEmail(request):
    serializer = EducationSignUpSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = 'New Sign Up \n Education \n\n ' + fullName + '\n' + email
    if serializer.is_valid():
        send_mail('SmartFarma SignUp HURRY', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def ContactEmail(request):
    serializer = ContactEmailSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    companyName = data.get('companyName')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    message = data.get('message')

    if serializer.is_valid():
        send_mail('Malin Greats Contact Form', fullName + '\n' + companyName + '\n' + email + '\n' + phoneNumber + '\n' + '\n\n' + message, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def EnquiryEmail(request):
    serializer = EnquiryEmailSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = fullName + '\n' + email
    if serializer.is_valid():
        send_mail('Malin Greats Enquiry', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def Newsletter(request):
    serializer = NewsletterSerializer(data=request.data)
    data = request.data
    email = data.get('email')
    body = 'Hello' + '\n' + email + 'just joined the newsleter mail list'
    if serializer.is_valid():
        send_mail('Malin Newsletter Subscriptions', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def Quotation(request):
    serializer = QuotationSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = fullName + '\n' + email + '\n Asking for a quotation'
    if serializer.is_valid():
        send_mail('MG Smart Systems Qoutation', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)
