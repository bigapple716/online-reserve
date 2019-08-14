from django.db import models
import datetime


# Create your models here.
class Applicant(models.Model):
    # fields
    name = models.CharField(max_length=10, help_text='请输入您的姓名')
    gov_id = models.CharField(max_length=18, primary_key=True, help_text='请输入您的身份证号')
    contact = models.IntegerField(help_text='请输入您的联系方式')

    choices = (
        (datetime.date(year=2019, month=9, day=1), '2019-09-01'),
        (datetime.date(year=2019, month=9, day=2), '2019-09-02'),
    )
    date = models.DateField(choices=choices)
