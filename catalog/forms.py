from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Applicant, Service


class ReservationForm(forms.ModelForm):
    # automatically generated from the model in models.py
    class Meta:
        model = Applicant
        fields = '__all__'
        labels = {'name': '姓名', 'gov_id': '身份证号', 'contact': '联系方式', 'date': '预约时段'}

    # check gov_id
    def clean_gov_id(self):
        data = self.cleaned_data['gov_id']

        # check length
        if len(data) != 18:
            raise ValidationError('无效身份证号！')

        # check format
        if data.isdigit() or (data[:-1].isdigit() and (data[-1] == 'x' or data[-1] == 'X')):
            pass
        else:
            raise ValidationError('无效身份证号！')

        return data

    # check date
    def clean_date(self):
        data = self.cleaned_data['date']

        threshold = list(Service.objects.filter(date__exact=data))[0].quota

        same_date = list(Applicant.objects.filter(date__exact=data))
        if len(same_date) >= threshold:
            raise ValidationError('该时间段已约满，请选择其他时间段！')

        return data


class InquiryForm(forms.Form):
    gov_id = forms.CharField(max_length=18, label='身份证号')

    # check gov_id
    def clean_gov_id(self):
        data = self.cleaned_data['gov_id']

        # check length
        if len(data) != 18:
            raise ValidationError('无效身份证号！')

        # check format
        if data.isdigit() or (data[:-1].isdigit() and (data[-1] == 'x' or data[-1] == 'X')):
            pass
        else:
            raise ValidationError('无效身份证号！')

        return data
