# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clanguage(models.Model):
	isbn = models.IntegerField(primary_key=True) #with primary key
	author = models.CharField(max_length=200)
	bookname = models.IntegerField()

	class Meta:
		db_table="cdetails"

