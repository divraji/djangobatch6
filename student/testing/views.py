# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from testing.models import studentdb
from django.http import HttpResponse
import os, time
from django.conf import settings
# Create your views here.
def viewhome(request):
	return render(request, "testing/home.html")

def viewstudentinfo(request):
	s_inst = studentdb.objects.all()
	return render(request, "testing/displayinfo.html", {"data":s_inst})

def viewaddstudent(request):
	if request.method == "POST":
		data = request.POST

		if data.get("addnew"):
			pic = request.FILES['studpic']
			picname = str(time.time())+pic.name
			f=open(os.path.join(settings.MEDIA_ROOT, picname),'wb')
			for chunk in pic.chunks():
				f.write(chunk)
			f.close()

			ns = studentdb(name=data.get("name"),course = data.get("course"))
			ns.studpic = picname
			ns.save()
			return redirect(viewhome)

	return render(request, "testing/addinfo.html")

def viewmngstudent(request):
	s_inst = studentdb.objects.all()
	return render(request, "testing/manageinfo.html", {"data":s_inst})

def viewstudupdate(request,pk):
	s_inst = studentdb.objects.get(pk=pk)
	if request.method == "POST":
		data = request.POST

		s_inst.name = data.get("name")
		s_inst.course = data.get("course")

		s_inst.save()
		return redirect(viewmngstudent)	

	return render(request,"testing/studupdate.html", {"data":s_inst})

def viewstuddelete(request,pk):
	s_inst = studentdb.objects.get(pk=pk)
	if request.method == "POST":
		s_inst.delete()
		return redirect(viewmngstudent)	
	return render(request,"testing/studdelete.html", {"data":s_inst})

