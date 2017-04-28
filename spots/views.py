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
		data = json.loads(request.body.decode("utf-8"))
		with open('data.txt', 'w') as outfile:
			json.dump(data, outfile)
			return HttpResponse(data)
    else:
    	#data = json.loads(request.body.decode("utf-8"))
    	#with open('data.txt', 'w') as outfile:
		#	json.dump(data, outfile)
    	return HttpResponse("POST request not valid")
    return HttpResponse("No json data")



def get_data(request):
	#global json_received
	with open('data.txt') as json_file:  
		data = json.load(json_file)
		if data:
			#print request.session['results']
			#json_received = request.session.get('results')
			return JsonResponse(data, safe=False)
		else:
			#print json_received
			#json_received = request.session.get('results')
			return JsonResponse(data, safe=False)




