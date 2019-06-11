from django.http import HttpResponse
from django.shortcuts import render
from empire.models import UserLogin , ShopDetails , FeedBackDetails
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly ,BasePermission , SAFE_METHODS
from django.forms.models import model_to_dict

import json

from rest_framework import viewsets
from .serializers import UserLoginSerializer, ShopDetailserializer ,FeedBackDetailsSerializer
from rest_framework.views import APIView, Response

responseDictionary = {'requestKey':None,'queueData':None,'transactionId':None}

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

def index(request):
    date_modified = datetime.now()
    shopDetails = ShopDetails.objects.all()
    try:
        for i in shopDetails:
            i.address1 = i.address1.replace(",","\n")
        return render(request, 'empire/home.html', {'shop':shopDetails})
    except:
        return HttpResponse("404 Not Found")
 
class UserLoginViewSet(viewsets.ModelViewSet):        
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer
        
class ShopDetailsViewSet(viewsets.ModelViewSet):
    queryset = ShopDetails.objects.all()
    serializer_class = ShopDetailserializer

class FeedBackDetailsViewSet(viewsets.ModelViewSet):
    queryset = FeedBackDetails.objects.all()
    serializer_class = FeedBackDetailsSerializer 
    http_method_names = ['post']   


class CustomView(APIView):
    permission_classes = (IsAuthenticated, ReadOnly)
    def get(self, request, format=None):
        queryset = ShopDetails.objects.all()
        return Response("cool")
    def post(self, request, format=None):
        return Response("Some Post Response")    


@api_view(['POST'])
def footerDetails(request):        
    permission_classes = (IsAuthenticated,ReadOnly)
    if request.method == 'POST':
        responseDictionary['statusCode']=200
        responseDictionary['statusMessage']='Success'
        responseDictionary['data'] = {}
        for question in ShopDetails.objects.all():
            # question_representation = {'about_us': question.about_us,
            #     'address1': question.address1}
            question_representation = model_to_dict(question)
            responseDictionary['data'].update(question_representation)
        return HttpResponse(json.dumps(responseDictionary), content_type='application/json')
    else:    
        responseDictionary['statusCode']=404
        responseDictionary['statusMessage']='Failure'
        responseDictionary['data']='Method Not Allowed'
        return HttpResponse(json.dumps(responseDictionary), content_type='application/json')        