# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Service(models.Model):
    # fields
    date = models.CharField(max_length=100, primary_key=True)
    quota = models.IntegerField(default=0)  # 该时间段的总名额


class Applicant(models.Model):
    # fields
    name = models.CharField(max_length=10, help_text='')
    gov_id = models.CharField(max_length=18, primary_key=True, help_text='')
    contact = models.IntegerField(help_text='')

    choices = []
    for elem in list(Service.objects.all()):
        c = (elem.date, elem.date)
        choices.append(c)

    date = models.CharField(max_length=100, choices=choices)



