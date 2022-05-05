from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.mail import send_mail
import datetime


from .serializers import AgricultureDomainSerializer, AgricultureSignUpSerializer, RetailSignUpSerializer, EducationSignUpSerializer, ContactEmailSerializer, EnquiryEmailSerializer, NewsletterSerializer, QuotationSerializer, HealthcareSignUpSerializer, ManufacturingSignUpSerializer, ManufacturingDomainSerializer, HealthcareDomainSerializer, EducationDomainSerializer, RetailDomainSerializer, TotalDomainSerializer, TotalSignUpSerializer
from .models import AgricultureDomain, AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter, Quotation, HealthcareSignUp, ManufacturingSignUp, ManufacturingDomain, HealthcareDomain, EducationDomain, RetailDomain, TotalSignUp, TotalDomain


@api_view(['POST'])
def addAgricultureDomain(request):
    serializer = AgricultureDomainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def addRetailDomain(request):
    serializer = RetailDomainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def addEducationDomain(request):
    serializer = EducationDomainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def addManufacturingDomain(request):
    serializer = ManufacturingDomainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def addHealthcareDomain(request):
    serializer = HealthcareDomainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['GET'])
def getFreeDomains(request):
    qs = AgricultureDomain.objects.filter(isOccupied=False)
    print(qs[1])
    serializer = AgricultureDomainSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def AgricSignUpEmail(request):
    serializer = AgricultureSignUpSerializer(data=request.data)
    domains = AgricultureDomain.objects.filter(isOccupied=False)

    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    domainName = domains[1].name
    fullDomain = AgricultureDomain.objects.get(name=domainName)

    signUps = AgricultureSignUp.objects.filter(email=email)
    if signUps.exists():
        print('signUp exists')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        adminBody = 'New Sign Up \n\t Agriculture \n\n ' + fullName + '\n' + email
        clientBody = fullName + ' Welcome to SmartAgriculture \n' + \
            'Navigate to the link below and register your account \n\n' 'http://' + domainName
        if serializer.is_valid():
            send_mail('SmartFarma SignUp HURRY', adminBody, 'malingreatsdev@gmail.com',
                      ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
            send_mail('Malin Greats Smart Farma', clientBody, 'malingreatsdev@gmail.com',
                      [email], fail_silently=False)
            serializer.save()

            qs = AgricultureSignUp.objects.get(email=email)
            qs.domain = fullDomain
            qs.save()

            query = TotalSignUp.objects.get(id=1)
            query.agricultureTotal += 1
            query.save()

        else:
            return Response('serializer not valid')
        return Response(serializer.data)


@api_view(['POST'])
def RetailSignUpEmail(request):
    serializer = RetailSignUpSerializer(data=request.data)
    domains = RetailDomain.objects.filter(isOccupied=False)

    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    domainName = domains[1].name
    fullDomain = RetailDomain.objects.get(name=domainName)

    signUps = RetailSignUp.objects.filter(email=email)
    if signUps.exists():
        print('signUp exists')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        adminBody = 'New Sign Up \n\t Retail \n\n ' + fullName + '\n' + email
        clientBody = fullName + ' Welcome to SmartRetail \n' + \
            'Navigate to the link below and register your account \n\n' 'http://' + domainName
        if serializer.is_valid():
            send_mail('SmartRetail SignUp HURRY', adminBody, 'malingreatsdev@gmail.com',
                      ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
            send_mail('Malin Greats Smart Farma', clientBody, 'malingreatsdev@gmail.com',
                      [email], fail_silently=False)
            serializer.save()

            qs = RetailSignUp.objects.get(email=email)
            qs.domain = fullDomain
            qs.save()

            query = TotalSignUp.objects.get(id=1)
            query.retailTotal += 1
            query.save()

        else:
            return Response('serializer not valid')
        return Response(serializer.data)


@api_view(['POST'])
def EduSignUpEmail(request):
    serializer = EducationSignUpSerializer(data=request.data)
    domains = EducationDomain.objects.filter(isOccupied=False)

    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    domainName = domains[1].name
    fullDomain = EducationDomain.objects.get(name=domainName)

    signUps = EducationSignUp.objects.filter(email=email)
    if signUps.exists():
        print('signUp exists')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        adminBody = 'New Sign Up \n\t Education \n\n ' + fullName + '\n' + email
        clientBody = fullName + ' Welcome to SmartEducation \n' + \
            'Navigate to the link below and register your account \n\n' 'http://' + domainName
        if serializer.is_valid():
            send_mail('SmartEducation SignUp HURRY', adminBody, 'malingreatsdev@gmail.com',
                      ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
            send_mail('Malin Greats Smart Farma', clientBody, 'malingreatsdev@gmail.com',
                      [email], fail_silently=False)
            serializer.save()

            qs = EducationSignUp.objects.get(email=email)
            qs.domain = fullDomain
            qs.save()

            query = TotalSignUp.objects.get(id=1)
            query.educationTotal += 1
            query.save()

        else:
            return Response('serializer not valid')
        return Response(serializer.data)


@api_view(['POST'])
def HealthcareSignUpEmail(request):
    serializer = HealthcareSignUpSerializer(data=request.data)
    domains = HealthcareDomain.objects.filter(isOccupied=False)

    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    domainName = domains[1].name
    fullDomain = HealthcareDomain.objects.get(name=domainName)

    signUps = HealthcareSignUp.objects.filter(email=email)
    if signUps.exists():
        print('signUp exists')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        adminBody = 'New Sign Up \n\t Healthcare \n\n ' + fullName + '\n' + email
        clientBody = fullName + ' Welcome to SmartHealthcare \n' + \
            'Navigate to the link below and register your account \n\n' 'http://' + domainName
        if serializer.is_valid():
            send_mail('SmartFarma SignUp HURRY', adminBody, 'malingreatsdev@gmail.com',
                      ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
            send_mail('Malin Greats Smart Farma', clientBody, 'malingreatsdev@gmail.com',
                      [email], fail_silently=False)
            serializer.save()

            qs = HealthcareSignUp.objects.get(email=email)
            qs.domain = fullDomain
            qs.save()

            query = TotalSignUp.objects.get(id=1)
            query.healthcareTotal += 1
            query.save()

        else:
            return Response('serializer not valid')
        return Response(serializer.data)


@api_view(['POST'])
def ManufacturingSignUpEmail(request):
    serializer = ManufacturingSignUpSerializer(data=request.data)
    domains = ManufacturingDomain.objects.filter(isOccupied=False)

    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    domainName = domains[1].name
    fullDomain = ManufacturingDomain.objects.get(name=domainName)

    signUps = ManufacturingSignUp.objects.filter(email=email)
    if signUps.exists():
        print('signUp exists')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        adminBody = 'New Sign Up \n\t Manufacturing \n\n ' + fullName + '\n' + email
        clientBody = fullName + ' Welcome to SmartManufacturing \n' + \
            'Navigate to the link below and register your account \n\n' 'http://' + domainName
        if serializer.is_valid():
            send_mail('SmartFarma SignUp HURRY', adminBody, 'malingreatsdev@gmail.com',
                      ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
            send_mail('Malin Greats Smart Farma', clientBody, 'malingreatsdev@gmail.com',
                      [email], fail_silently=False)
            serializer.save()

            qs = ManufacturingSignUp.objects.get(email=email)
            qs.domain = fullDomain
            qs.save()

            query = TotalSignUp.objects.get(id=1)
            query.manufacturingTotal += 1
            query.save()

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


@api_view(['GET'])
def getAgriSignUps(request):
    qs = AgricultureSignUp.objects.all()
    serializer = AgricultureSignUpSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRetailSignUps(request):
    qs = RetailSignUp.objects.all()
    serializer = RetailSignUpSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEduSignUps(request):
    qs = EducationSignUp.objects.all()
    serializer = EducationSignUpSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getManuSignUps(request):
    qs = ManufacturingSignUp.objects.all()
    serializer = ManufacturingSignUpSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getHealthSignUps(request):
    qs = HealthcareSignUp.objects.all()
    serializer = HealthcareSignUpSerializer(qs, many=True)
    return Response(serializer.data)
