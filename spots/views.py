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
from os.path import join
@csrf_exempt
def upload(request):
    #global json_received
    if request.method == "POST":
		data = request.body.decode("utf-8")
		print data
		spot_form = SpotForm(request.POST, request.FILES)
		print "fucking spot"
		if spot_form.is_valid():
			#spot = Spot()
			#spot.report = spot_form.cleaned_data["report"]
			#print data
			#spot.save()
			spot_form.save()
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
	data = Spot.objects.all()[0]
	print data
	return JsonResponse(data, safe=False)
	'''if data is not None:
		#print request.session['results']
		#json_received = request.session.get('results')
		j_obj = json.load(data)
		print j_obj
		#return JsonResponse(data, safe=False)
	else:
		#print json_received
		#json_received = request.session.get('results')
		#return JsonResponse(data, safe=False)
		pass
	return HttpResponse("No json data")
	'''



