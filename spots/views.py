from django.shortcuts import render
from django.core import serializers

#from django.utils import simplejson

# Create your views here.

import json
from django.http import HttpResponse
from django.http import JsonResponse



json_received1 = {
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

def upload(request):
	global json_received
	if request.method == "POST":
		#json_received = json.loads(request.body.decode("utf-8"))
		request.session['data'] = json.loads(request.body.decode("utf-8"))
        return HttpResponse("Got json data")
    #return HttpResponse("POST request not valid")



def get_data(request):
	#global json_received
	if json_received is None:
		return JsonResponse(request.session.get('data'), safe=False)
	else:
		return JsonResponse(json_received, safe=False)




