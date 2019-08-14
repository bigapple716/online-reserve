from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import ReservationForm, InquiryForm
from .models import Applicant


# home page
def index(request):
    return render(request, 'index.html')


# reserve
def reserve(request):
    applicant = Applicant()

    if request.method == 'POST':
        # If this is a POST request then process the Form data
        # Create a form instance and populate it with data from the request (binding):
        form = ReservationForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # transfer the data from form to applicant
            applicant.name = form.cleaned_data['name']
            applicant.gov_id = form.cleaned_data['gov_id']
            applicant.contact = form.cleaned_data['contact']
            applicant.date = form.cleaned_data['date']
            applicant.save()

            # redirect to URL:
            return HttpResponseRedirect(reverse('reserve-success'))

        # else:
        #     return render(request, 'catalog/reserve-fail.html', {'err_msg': })

    else:
        # request.method != 'POST'
        # 当什么信息都没有提交的时候，显示空白输入框
        form = ReservationForm(initial={})

    return render(request, 'catalog/reserve.html', {'form': form})


# reserve-success
def reserve_success(request):
    return render(request, 'catalog/reserve-success.html')


# inquiry
def inquiry(request):
    if request.method == 'POST':
        # If this is a POST request then process the Form data
        form = InquiryForm(request.POST)

        if form.is_valid():
            applicant_list = list(Applicant.objects.filter(gov_id__exact=form.cleaned_data['gov_id']))
            if len(applicant_list) != 0:
                # when applicant_list is not empty, get the 1st (only) element
                return render(request, 'catalog/inquiry-success.html', {'reserve_date': applicant_list[0].date})
            else:
                # when applicant_list is empty, inquiry is failed
                return render(request, 'catalog/inquiry-fail.html')

    else:
        # request.method != 'POST'
        # 当什么信息都没有提交的时候，显示空白输入框
        form = InquiryForm(initial={})

    return render(request, 'catalog/inquiry.html', {'form': form})


# inquiry-success
def inquiry_success(request):
    return render(request, 'catalog/inquiry-success.html')
