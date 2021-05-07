# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#$ python manage.py sqlmigrate polls 0001

class Usuario(models.Model):
    login = models.CharField(max_length=200)
    
# Create your models here.
