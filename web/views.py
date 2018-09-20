from django.shortcuts import render
from django.http import HttpResponse
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def login(request):
    
    print('login process')
    print(request.POST)

    return JsonResponse({
        'status' : 'OK',
    }, encoder=JSONEncoder)
    