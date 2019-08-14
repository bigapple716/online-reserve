from django.contrib import admin
from .models import Applicant
from import_export.admin import ExportActionMixin


class ApplicantAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['date']


# Register your models here.
admin.site.register(Applicant, ApplicantAdmin)
