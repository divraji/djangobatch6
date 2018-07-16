# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StudyHall(models.Model):
	name=models.CharField(max_length=50)
	area=models.TextField()

	class Meta:
		db_table="mystudyhall"

class Enquiry(models.Model):
	name=models.CharField(max_length=50)
	contactnumber=models.IntegerField()
	course=models.CharField(max_length=50)

	class Meta:
		db_table="myenquiry"

class Expense(models.Model):
	name=models.CharField(max_length=50)
	dateofexp=models.DateField()
	readroomname=models.CharField(max_length=50)
	sumexp=models.IntegerField()

	class Meta:
		db_table="myexpense"