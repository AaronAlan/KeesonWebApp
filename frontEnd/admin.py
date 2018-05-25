from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Bed)
admin.site.register(Patient)
admin.site.register(PatientMH)
admin.site.register(PatientTE)
admin.site.register(PatientLB)
admin.site.register(PatientEX)
admin.site.register(PatientPR)
admin.site.register(PatientPE)

