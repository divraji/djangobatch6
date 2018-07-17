# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import Course,StudyHall,Expenses,Student,Enquiry
# Register your models here.

admin.site.register(Course)
admin.site.register(StudyHall)
admin.site.register(Expenses)
admin.site.register(Student)
admin.site.register(Enquiry)
