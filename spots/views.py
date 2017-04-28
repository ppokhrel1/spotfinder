from django.shortcuts import render
from django.core import serializers

#from django.utils import simplejson

# Create your views here.

import json
from django.http import HttpResponse
from django.http import JsonResponse


'''
json_received = {
	"results":[
		{
			"name" : "something",
			"color" : "green"
		},
		{
			"name" : "something",
			"color" : "red"
		},
		{
			"name" : "something",
			"color" : "red"
		},
		{
			"name" : "something",
			"color" : "red"
		}
	]
}
'''
from .helpers import create_or_update_and_get
from .models import *

def upload(request):
	if request.method == "POST":
		json_received["results"] = json.loads( request.body.decode("utf-8") )
		objects = create_or_update_and_get(Data, json_received)
		return HttpResponse("Got json data")
	else:
		return HttpResponse("No json data")
	return HttpResponse("POST request not valid")



def get_data(request):
	data = Data.objects.all()[-1: -5]
	results = {}
	results['results'] = data
	return JsonResponse(results, safe=False)



