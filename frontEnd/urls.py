from django.urls import path

from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('display_page/', views.displaypage, name='displayPage'),
    path('add_people/', views.addpeople, name='addPerson'),
    path('add_med_history/', views.addmedhistory, name='addMedHis'),
    path('add_day_diag/', views.adddaydiag, name='addDayDiag'),
    path('add_rad_report/', views.addradreport, name='addRadReport'),
    path('add_drug_history/', views.adddrughistory, name='addDrugHistory'),
    path('add_surg_history/', views.addsurghistory, name='addSurgHistory'),
    path('add_body_status/', views.addbodystatus, name='addBodyStatus'),
    path('bed_detail/<str:device_id>/', views.beddetail, name='bedDetail'),
]
