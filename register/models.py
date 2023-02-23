from django.db import models
from django.urls import reverse_lazy as _

from store.constant import STATE_CHOICES
# from django.contrib.localflavor.us.us_states import STATE_CHOICES


class Register(models.Model):	
	name = models.CharField(max_length=200,)
	cell_main = models.CharField(max_length=11, blank = True)
	cell_contact = models.CharField(max_length=11, blank = True)
	email = models.EmailField(max_length=254, blank=True)
	document = models.CharField(max_length=21, blank = True)
	street = models.CharField(max_length=200, blank=True,)
	number = models.CharField(max_length=30,blank=True)
	zipcode = models.CharField(max_length=11,blank=True)
	state = models.CharField(choices = STATE_CHOICES, max_length=2, blank=True)
	city = models.CharField(max_length=100,blank=True)	
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name
	
	def register_gau_detail(self):
		return _('register:register_details', args=[self.pk])

	def register_gau_edit(self):
		return _('register:register_update', args=[self.pk])

	def register_gau_delete(self):
		return _('register:register_delete', args=[self.pk])