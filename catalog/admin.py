from django.contrib import admin
from .models import Applicant, Service
from import_export.admin import ExportActionMixin


class ApplicantAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['date']


class ServiceAdmin(ExportActionMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Service, ServiceAdmin)
