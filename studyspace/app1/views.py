# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import StudyHall
from app1.models import Enquiry
from app1.models import Expense

# Create your views here.
def viewindex(request):
	return render(request,"app1/index.html")

def viewstudyhalls(request):
	shalls=StudyHall.objects.all()
	return render(request, "app1/index.html", {"data":shalls})

def viewenquiry(request):
	enq=Enquiry.objects.all()
	return render(request, "app1/index.html", {"enqdata":enq})

def viewexpenses(request):
	exp=Expense.objects.all()
	return render(request, "app1/index.html",{"expdata": exp})