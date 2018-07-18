# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import StudyHall,Expenses,Enquiry
# Create your views here.
def viewindex(request):
	if request.method == "POST":
		#import pdb;pdb.set_trace()
		data=request.POST
		hall=StudyHall(name=data.get("hall_name"),area=data.get("hall_area"))
		hall.save()
	studyhalls = StudyHall.objects.all()
	exp = Expenses.objects.all()
	enq = Enquiry.objects.all()

	return render(request,"app1/index.html" ,{
		"datahalls": studyhalls,
		"dataexps": exp,
		"dataenqs": enq
		})

