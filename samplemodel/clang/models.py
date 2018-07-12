# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clocation(models.Model):
	location = models.CharField(max_length=250)
	pincode = models.IntegerField()

	class Meta:
		db_table="carea"

class Clanguage(models.Model):
	isbn = models.IntegerField(primary_key=True) #with primary key
	author = models.CharField(max_length=200)
	bookname = models.IntegerField()

	class Meta:
		db_table="cdetails"

class Clanguagesales(models.Model):
	salesmode=[('shop', 'Visited Shop'), ('web', 'Online Sales')]
	copies = models.IntegerField()
	bookname = models.ForeignKey(Clanguage)
	location = models.ManyToManyField(Clocation)
	mode_sales = models.CharField(choices=salesmode , max_length=6)

	class Meta:
		db_table="csales"

