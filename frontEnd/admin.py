from django.contrib import admin

# Register your models here.
from .models import *


class PatientBedAdmin(admin.ModelAdmin):
    search_fields = ['BEDID']


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


admin.site.register(PatientBed, PatientBedAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientMH, PatientMHAdmin)
admin.site.register(PatientTE, PatientTEAdmin)
admin.site.register(PatientLB, PatientLBAdmin)
admin.site.register(PatientEX, PatientEXAdmin)
admin.site.register(PatientPR, PatientPRAdmin)
admin.site.register(PatientPE, PatientPEAdmin)


class RonghuaBedAdmin(admin.ModelAdmin):
    search_fields = ['BEDID']


class DM_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'DMGENDER', 'DMSTDTC', 'DMENDTC']
    list_filter = ['BEDID']
    search_fields = ['BEDID']


class EX_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'EXDATE']
    list_filter = ['BEDID', 'EXDATE']
    search_fields = ['BEDID']


class NU_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'NUCATE', 'NUDATE']
    list_filter = ['BEDID', 'NUDATE']
    search_fields = ['BEDID']


class PE_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'PECATE', 'PEDATE']
    list_filter = ['BEDID', 'PEDATE']
    search_fields = ['BEDID']


class BB_RonghuaAdmin(admin.ModelAdmin):
    list_display = ['BEDID', 'SUBJECTID', 'BBCATE', 'BBDATE']
    list_filter = ['BEDID', 'BBDATE']
    search_fields = ['BEDID']


admin.site.register(RonghuaBed, RonghuaBedAdmin)
admin.site.register(DM_Ronghua, DM_RonghuaAdmin)
admin.site.register(EX_Ronghua, EX_RonghuaAdmin)
admin.site.register(NU_Ronghua, NU_RonghuaAdmin)
admin.site.register(PE_Ronghua, PE_RonghuaAdmin)
admin.site.register(BB_Ronghua, BB_RonghuaAdmin)
