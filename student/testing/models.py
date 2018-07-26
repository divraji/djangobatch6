# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class studentdb(models.Model):
	name = models.CharField(max_length=200)
	course = models.CharField(max_length=150)
	studpic = models.ImageField(default="logo.png",blank=True, null=True)

	def __str__(self):
		return "%s %s" % (self.name,self.course)