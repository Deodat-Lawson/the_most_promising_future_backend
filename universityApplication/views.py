from django.shortcuts import render
import openai, os, json
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from django.http import JsonResponse
from openai import OpenAI

from universityApplication.serializers import personalStatusFormSerializer
from universityApplication.gpt_api import chatbot
from rest_framework import viewsets

from universityApplication.models import personalStatusForm


class PersonalStatusFormViewSet(viewsets.ModelViewSet):
  queryset = personalStatusForm.objects.all()
  serializer_class = personalStatusFormSerializer


@csrf_exempt
def handleRequest(request):
    print('got request')
    print('Request method:', request.method)
    data = {'key': 'value'}
    return_response = data  # Initialize return_response with a default value

    if request.method == 'POST':
        print(f'POST request: {json.loads(request.body)}')
        body = json.loads(request.body)  # Load the JSON request body

        thisPerson = personalStatusForm.objects.create(
            fullName=body.get('fullName'),
            currentGradeLevel=body.get('currentGradeLevel'),
            locationOfResidence=body.get('country'),
            citizenship=body.get('citizenship'),
            currentSchoolSystem=body.get('currentSchoolSystem'),
            GPA=body.get('GPA'),
            SAT=body.get('SAT'),
            ACT=body.get('ACT'),
            honorsAndAwards=body.get('honorAndAwards'),
            fieldsOfInterest=body.get('fieldsOfInterest'),
            geographicPreferences=body.get('geographicalPreference'),
            sizeOfUniversity=body.get('sizeOfUniversity'),
            prestigeFactor=body.get('prestigeFactor'),
            financialAid=body.get('requireFinancialAidScale'),
            EA=body.get('EA'),
            ED=body.get('ED'),
            RD=body.get('RD'),
            numberOfSchools=body.get('numberOfSchools')
        )

        return_response = chatbot(thisPerson)

    return JsonResponse(return_response, safe=False)
