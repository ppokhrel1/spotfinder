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
from django.conf import settings
def upload(request):
    #global json_received
    if request.method == "POST":
        #json_received = json.loads(request.body.decode("utf-8"))
        #request.session['results'] = json_received
        settings.JSON = json.loads(request.body.decode("utf-8"))
        return HttpResponse(settings.JSON)
    else:
    	settings.JSON = json.loads(request.body.decode("utf-8"))
    	return HttpResponse("POST request not valid")
    return HttpResponse("No json data")



def get_data(request):
	#global json_received
	if settings.JSON:
		#print request.session['results']
		#json_received = request.session.get('results')
		return JsonResponse(settings.JSON, safe=False)
	else:
		#print json_received
		#json_received = request.session.get('results')
		return JsonResponse(settings.JSON, safe=False)




