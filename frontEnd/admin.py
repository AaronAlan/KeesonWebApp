from django.contrib import admin

# Register your models here.
from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'DMGENDER', 'DMSTDTC', 'DMENDTC']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class PatientMHAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'MHDATE']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class PatientTEAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'TEDATE']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class PatientLBAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'LBDATE']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class PatientEXAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'EXDATE']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class PatientPRAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'PRDATE']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class PatientPEAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'PEDATE']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


admin.site.register(PatientBed)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientMH, PatientMHAdmin)
admin.site.register(PatientTE, PatientTEAdmin)
admin.site.register(PatientLB, PatientLBAdmin)
admin.site.register(PatientEX, PatientEXAdmin)
admin.site.register(PatientPR, PatientPRAdmin)
admin.site.register(PatientPE, PatientPEAdmin)

