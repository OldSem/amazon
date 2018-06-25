# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils import encoding
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime, date, time

from django.db import models

@python_2_unicode_compatible
class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    price = models.IntegerField()
    published = models.DateField(default=date.today)



    def __str__(self):
        return str(self.title)

# Create your models here.
