# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NameModel(models.Model):
	name = models.CharField(max_length=250, unique=True)

	class Meta:
		abstract=True

class StudyHall(NameModel):
	#name=models.CharField(max_length=50)
	area=models.TextField(max_length=250)

	def __str__(self):
		return "%s, %s" %(self.name,self.area)
class Expenses(NameModel):
	studyhall=models.ForeignKey(StudyHall)
	date=models.DateTimeField()
	#name=models.CharField(max_length=250)
	desc=models.TextField(max_length=250)
	value=models.IntegerField()

	def __str__(self):
		return "%s, %s, %s, %s" %(self.name,self.desc,self.value, self.date)

class Course(NameModel):
	#name=models.CharField(max_length=250)

	def __str__(self):
		return "%s" %(self.name)

class Student(NameModel):
	#name=models.CharField(max_length=250)
	address=models.TextField(max_length=250)
	phone=models.IntegerField()
	email=models.CharField(max_length=250)

	def __str__(self):
		return "%s--%s--%s--%s"%(self.name,self.address,self.phone,self.email)
class Enquiry(NameModel):
	#name=models.CharField(max_length=250)
	course=models.ForeignKey(Course)
	student=models.ForeignKey(Student)

	def __str__(self):
		return "%s,%s,%s" %(self.name,self.course,self.student)

class UserProfile(User):
	#It will create table in database app1_UserProfile
	#there is two coloumns role, User(onetoone relation with user model)
	roles = [("s", "student"), ("ss" , "studyspace")]
	role = models.CharField(choices=roles, max_length=2)
