# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CPluslanguage(models.Model):
	#id primary key created by django
	author = models.CharField(max_length=200)
	year = models.DateField()

	class Meta:
		db_table="cplusdetails"