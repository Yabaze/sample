from django.http import HttpResponse
from django.shortcuts import render
from empire.models import UserLogin , ShopDetails , FeedBackDetails
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

responseDictionary = {'requestKey':None,'queueData':None,'transactionId':None} 
def index(request):
    date_modified = datetime.now()
    b = UserLogin(first_name='T', middle_name = 'Mirakle',last_name='Yabaze',username = 'cool.mirakle@hotmail.com',password = '123456',created_time = date_modified)
    users = UserLogin.objects.all()
    shopDetails = ShopDetails.objects.all()
    try:
        for i in shopDetails:
            i.address1 = i.address1.replace(",","\n")
        return render(request, 'home.html', {'users': users,'shop':shopDetails})
    except:
        return HttpResponse("Data Saved Successfully")        

@api_view(['GET'])
def getShopDetails(request):
    try:
        responseDictionary['statusCode']=200
        responseDictionary['statusMessage']='Success'
        responseDictionary['data'] = {'users': 'users','shop':ShopDetails.objects.all()}
        response = JsonResponse(status = 200 , data = 'responseDictionary')
        return HttpResponse(response,content_type='application/json')
    except:
        responseDictionary['statusCode']=404
        responseDictionary['statusMessage']='Failure'
        responseDictionary['data']='No Data Found'
        response = JsonResponse(status = status.HTTP_200_OK, data = responseDictionary)
        print(response)
        return HttpResponse(response,content_type='application/json')
    # else:
    #     responseDictionary['statusCode']=405
    #     responseDictionary['statusMessage']='Failure'
    #     responseDictionary['data']='Method Not Allowed'
    #     response = JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, data = responseDictionary)
        
    # return HttpResponse(response,content_type='application/json')
                
