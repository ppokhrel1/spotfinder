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
def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x 
    return dict(map(ascii_encode, pair) for pair in data.items())


@csrf_exempt
def upload(request):
    #global json_received
    if request.method == "POST":
		data = json.loads(request.body.decode("utf-8"), object_hook=ascii_encode_dict)
		print data
		#d = Spot(report = str(data) )
		#d.report = str(data)
		#d.save()
		with open("file.json", 'w') as f:
			json.dump(data, f)
		return JsonResponse(data, safe=False)
    else:
    	#data = json.loads(request.body.decode("utf-8"))
    	#with open('data.txt', 'w') as outfile:
		#	json.dump(data, outfile)
    	return HttpResponse("POST request not valid")
    return HttpResponse("No json data")


def to_utf8(d):
    if type(d) is dict:
        result = {}
        for key, value in d.items():
            result[to_utf8(key)] = to_utf8(value)
    elif type(d) is unicode:
        return d.encode('utf8')
    else:
        return d


def get_data(request):
	print "puta"
	#with open('data.json', 'w') as f:
	#	data = json.load(f)
	f = open('file.json')
	print "yessica is a bitch"
	data = json.load(f)
	print data

	print "nothing"
	return JsonResponse(data, safe=False)
	#	return HttpResponse("No json data Bitch")
	#return HttpResponse("No json data Bitch")



