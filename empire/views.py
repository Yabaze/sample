from django.http import HttpResponse
from django.shortcuts import render
from empire.models import UserLogin , ShopDetails , FeedBackDetails
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

from rest_framework import viewsets
from .serializers import UserLoginSerializer, ShopDetailserializer ,FeedBackDetailsSerializer
from rest_framework.views import APIView, Response

responseDictionary = {'requestKey':None,'queueData':None,'transactionId':None} 
def index(request):
    date_modified = datetime.now()
    b = UserLogin(first_name='T', middle_name = 'Mirakle',last_name='Yabaze',username = 'cool.mirakle@hotmail.com',password = '123456',created_time = date_modified)
    users = UserLogin.objects.all()
    shopDetails = ShopDetails.objects.all()
    try:
        for i in shopDetails:
            i.address1 = i.address1.replace(",","\n")
        return render(request, 'home.html', {'users': ShopDetailserializer,'shop':shopDetails})
    except:
        return HttpResponse("Data Saved Successfully")        
 
class UserLoginViewSet(viewsets.ModelViewSet):        
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer
        
class ShopDetailsViewSet(viewsets.ModelViewSet):
    queryset = ShopDetails.objects.all()
    serializer_class = ShopDetailserializer    

class FeedBackDetailsViewSet(viewsets.ModelViewSet):
    queryset = FeedBackDetails.objects.all()
    serializer_class = FeedBackDetailsSerializer     
    http_method_names = ['get', 'post']   


class CustomView(APIView):
    def get(self, request, format=None):
        queryset = UserLogin.objects.all()
        return Response("cool")

    def post(self, request, format=None):
        return Response("Some Post Response")    


@api_view(['GET','POST'])
def questions_view(request):
    if request.method == 'GET':
        responseDictionary = {}
        responseDictionary['statusCode']=200
        responseDictionary['statusMessage']='Success'
        responseDictionary['data'] = {}
        for question in ShopDetails.objects.all():
            question_representation = {'about_us': question.about_us,'address1': question.address1}
            responseDictionary['data'].update(question_representation)
        return HttpResponse(json.dumps(responseDictionary), content_type='application/json')
    else:    
        responseDictionary = {}
        responseDictionary['statusCode']=404
        responseDictionary['statusMessage']='Failure'
        responseDictionary['data']='Method Not Allowed'
        return HttpResponse(json.dumps(responseDictionary), content_type='application/json')        