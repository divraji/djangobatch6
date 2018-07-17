# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StudyHall(models.Model):
	name=models.CharField(max_length=50)
	area=models.TextField(max_length=250)

	def __str__(self):
		return "%s, %s" %(self.name,self.area)
class Expenses(models.Model):
	studyhall=models.ForeignKey(StudyHall)
	date=models.DateTimeField()
	name=models.CharField(max_length=250)
	desc=models.TextField(max_length=250)
	value=models.IntegerField()

	def __str__(self):
		return "%s, %s, %s, %s" %(self.name,self.desc,self.value, self.date)

class Course(models.Model):
	name=models.CharField(max_length=250)

	def __str__(self):
		return "%s" %(self.name)

class Student(models.Model):
	name=models.CharField(max_length=250)
	address=models.TextField(max_length=250)
	phone=models.IntegerField()
	email=models.CharField(max_length=250)

	def __str__(self):
		return "%s--%s--%s--%s"%(self.name,self.address,self.phone,self.email)
class Enquiry(models.Model):
	name=models.CharField(max_length=250)
	course=models.ForeignKey(Course)
	student=models.ForeignKey(Student)

	def __str__(self):
		return "%s,%s,%s" %(self.name,self.course,self.student)