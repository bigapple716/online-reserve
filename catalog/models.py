# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Service(models.Model):
    # fields
    date = models.CharField(max_length=100, primary_key=True)  # 时间段
    quota = models.IntegerField(default=0)  # 该时间段的总名额


class Applicant(models.Model):
    # fields
    name = models.CharField(max_length=10, help_text='')  # 申请人姓名
    gov_id = models.CharField(max_length=18, primary_key=True, help_text='')  # 申请人身份证号
    contact = models.IntegerField(help_text='')  # 申请人联系方式

    choices = []
    for elem in list(Service.objects.all()):
        c = (elem.date, elem.date)
        choices.append(c)

    date = models.CharField(max_length=100, choices=choices)  # 预约的时间段



