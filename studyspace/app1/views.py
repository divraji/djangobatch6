# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import StudyHall,Expenses,Enquiry,Course,Student,UserProfile
from django.contrib.auth import authenticate

# Create your views here.
def viewindex(request):
	if request.method=="POST":
		data = request.POST

		if data.get("reg"):
			up = UserProfile.objects.create_user(
				username=data.get("username"),
				password=data.get("password"),
				email = data.get("email")
				)
			return render(request,"app1/index.html",
				{"msg":"USER created successfully!!. Please login"})
		else:
			user = authenticate(
				username = data.get("username"),
				password = data.get("password")
				)
			if user:
				return render(request,"app1/home.html",
					{"msg" :"Login successful"})
			else:
				return render(request,"app1/index.html",
					{"msg" :"Login Failed"})

	return render(request,"app1/index.html")
#	if request.method == "POST":
		#import pdb;pdb.set_trace()
#		data=request.POST
#		if data.get("studyhall"):
#			hall=StudyHall(name=data.get("hall_name"),area=data.get("hall_area"))
#			hall.save()
#		elif data.get("enquiry"):
#			name = data.get("enq_name")
#			course = data.get("enq_course")
#			student = data.get("enq_student")
#			course_inst = Course.objects.get(pk=course)
#			student_inst = Student.objects.get(pk=student)
#			enq_inst = Enquiry(name=name, course=course_inst,student = student_inst)
#			enq_inst.save()
#		elif data.get("expense"):
#			studyhall_inst = StudyHall.objects.get(pk=data.get("exp_studyhall"))
#			exp = Expenses(
#				studyhall = studyhall_inst,
#				date = data.get("exp_date"),
#				name = data.get("exp_name"),
#				desc = data.get("exp_desc"),
#				value = data.get("exp_value"),
#				)
#			exp.save()
#	studyhalls = StudyHall.objects.all()
#	exp = Expenses.objects.all()
#	enq = Enquiry.objects.all()
#	cour = Course.objects.all()
#	stud = Student.objects.all()
#
#	return render(request,"app1/index.html" ,{
#		"datahalls": studyhalls,
#		"dataexps": exp,
#		"dataenqs": enq,
#		"datacourse":cour,
#		"datastudent":stud
#		})


def viewhallupdate(request , pk):
	hall= StudyHall.objects.get(pk=pk)
	if request.method == "POST":
		data=request.POST
		hall.name=data.get("hall_name")
		hall.area=data.get("hall_area")
		hall.save()
		return redirect(viewstudyhalls)
	return render(request, "app1/hall_update.html", {"data": hall})

def viewhalldelete(request,hall_id):
	hall_info = StudyHall.objects.get(pk=hall_id)
	if request.method == "POST":
		data=request.POST
		hall_info.delete()
		return redirect(viewstudyhalls)
	return render(request, "app1/hall_delete.html", {"hall": hall_info})

def viewstudyhalls(request):
	data=request.POST
	if request.method == "POST":
		hall=StudyHall(name=data.get("hall_name"),area=data.get("hall_area"))
		hall.save()
	studyhalls = StudyHall.objects.all()
	return render(request, "app1/studyhall.html", {"datahalls":studyhalls})

def viewenquiries(request):
	data=request.POST
	if request.method == "POST":
		name = data.get("enq_name")
		course = data.get("enq_course")
		student = data.get("enq_student")
		course_inst = Course.objects.get(pk=course)
		student_inst = Student.objects.get(pk=student)
		enq_inst = Enquiry(name=name, course=course_inst,student = student_inst)
		enq_inst.save()
	enq = Enquiry.objects.all()
	cour = Course.objects.all()
	stud = Student.objects.all()
	return render(request, "app1/enquiry.html" , {"dataenqs":enq,
												  "datacourse":cour,
												  "datastudent":stud})

def viewreports(request):
	pass

