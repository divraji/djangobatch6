# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import StudyHall,Expenses,Enquiry,Course,Student
# Create your views here.
def viewindex(request):
	if request.method == "POST":
		#import pdb;pdb.set_trace()
		data=request.POST
		if data.get("studyhall"):
			hall=StudyHall(name=data.get("hall_name"),area=data.get("hall_area"))
			hall.save()
		elif data.get("enquiry"):
			name = data.get("enq_name")
			course = data.get("enq_course")
			student = data.get("enq_student")
			course_inst = Course.objects.get(pk=course)
			student_inst = Student.objects.get(pk=student)
			enq_inst = Enquiry(name=name, course=course_inst,student = student_inst)
			enq_inst.save()
		elif data.get("expense"):
			studyhall_inst = StudyHall.objects.get(pk=data.get("exp_studyhall"))
			exp = Expenses(
				studyhall = studyhall_inst,
				date = data.get("exp_date"),
				name = data.get("exp_name"),
				desc = data.get("exp_desc"),
				value = data.get("exp_value"),
				)
			exp.save()
	studyhalls = StudyHall.objects.all()
	exp = Expenses.objects.all()
	enq = Enquiry.objects.all()
	cour = Course.objects.all()
	stud = Student.objects.all()

	return render(request,"app1/index.html" ,{
		"datahalls": studyhalls,
		"dataexps": exp,
		"dataenqs": enq,
		"datacourse":cour,
		"datastudent":stud
		})

