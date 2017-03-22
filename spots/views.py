from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse
from django.http import JsonResponse


json_received = ''
def upload(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))

        return HttpResponse("Got json data")
    return HttpResponse("POST request not valid")



def get_data(request):
    return JsonResponse(json_received, safe=False)



