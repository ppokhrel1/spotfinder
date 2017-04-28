from django.db import models
import collections

# Create your models here.
#class Data(models.Model):
#	#name = models.CharField(max_length = 100)
#	#color = models.CharField(max_length = 100)
#	#json = JSONField()
#	json = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
#	#json = models.CharField(max_length = 400)


class Spot(models.Model):
	#names = models.CharField(max_length = 100, default = '')
	report = models.CharField(max_length = 500, default = '')
	#report = models.FileField(db_index=True, upload_to='not_used')
#class Data(models.Model):
#	mydata = models.ManyToManyField(Spot)