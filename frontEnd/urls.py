from django.urls import path

from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('display_page/', views.displaypage, name='displayPage'),
    path('bed_add_details/<int:bed_id>/', views.bedadddetails, name='bedAddDetails'),
    path('add_people/<int:bed_id>/', views.addpeople, name='addPerson'),
    path('add_med_history/<int:bed_id>/', views.addmedhistory, name='addMedHis'),
    path('add_day_diag/<int:bed_id>/', views.adddaydiag, name='addDayDiag'),
    path('add_rad_report/<int:bed_id>/', views.addradreport, name='addRadReport'),
    path('add_drug_history/<int:bed_id>/', views.adddrughistory, name='addDrugHistory'),
    path('add_surg_history/<int:bed_id>/', views.addsurghistory, name='addSurgHistory'),
    path('add_body_status/<int:bed_id>/', views.addbodystatus, name='addBodyStatus'),
    path('bed_detail/<str:device_id>/', views.beddetail, name='bedDetail'),
]
