from django.shortcuts import render
from django.core import serializers

#from django.utils import simplejson

# Create your views here.

import json
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
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
from models import Spot
from django.core import serializers
from forms import SpotForm
@csrf_exempt
def upload(request):
    #global json_received
    if request.method == "POST":
		data = request.body.decode("utf-8")
		print data
		d = Spot(report = str(data) )
		#d.report = str(data)
		d.save()
		print d
		#data = Data(json=str(data))
		#for fields in data:
		#	json_format =
		#json_var = json.loads(data)
		#for j, i in json_var.iteritems():
			#print json_var[i]
			#Spot(json_var[i])
			
			#print i
		#	for x in i:
		#		d = SpotForm(x)#name=x['name'], color = x['color'])
		#		#print x['color']
		#		#d.name = x['name']
		#		#d.color = x['color']
		#		if d.is_valid():
		#			d = d.save(commit=False)
		#			d.save()
		#	#for k, v in i.iteritems():
		#	#	setattr(d, k.lower(), v)
		#	#d.save()
		#data.save()
		#request.session['fav_color'] = data

		#with open('data.txt', 'w') as outfile:
		#	json.dump(data, outfile)
		return JsonResponse(data, safe=False)
    else:
    	#data = json.loads(request.body.decode("utf-8"))
    	#with open('data.txt', 'w') as outfile:
		#	json.dump(data, outfile)
    	return HttpResponse("POST request not valid")
    return HttpResponse("No json data")



def get_data(request):
	#global json_received
	#with open('data.txt') as json_file:  
	#	data = json.loads(json_file)
	#data = request.session.get('fav_color')
	data = Spot.objects.order_by('id')[0]
	if data is not None:
		#print request.session['results']
		#json_received = request.session.get('results')
		return JsonResponse(data, safe=False)
	else:
		#print json_received
		#json_received = request.session.get('results')
		return JsonResponse(data, safe=False)




