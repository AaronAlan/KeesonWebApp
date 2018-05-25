# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import pymysql

# Create your views here.
@login_required
def homepage(request):
    curUser = get_object_or_404(User, pk=request.user.id)
    if curUser.username == "jiaxingyiyuan":
        # form = BedForm(request.POST)
        # if request.method == 'POST' and form.is_valid():
        #     newBed = Bed.objects.create(bed_name=form.cleaned_data['bed_name'])
        #     newBed.save()
        # newForm = BedForm()
        # bedSet = Bed.objects.all()
        return render(request, 'yiyuan_homepage.html')
    elif curUser.username == "ronghua":
        return render(request, 'ronghua_homepage.html')


@login_required
def displaypage(request):
    try:
        conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "softide_cloud2", charset="utf8")
        print("Successful connection to db softide_cloud2")
    except:
        print("Failed to connect to db softide_cloud2")
        return HttpResponseRedirect(reverse('homepage'))
    cur = conn.cursor()
    bedQuery = "SELECT serial_number, device_id FROM sc_app_beds;"
    cur.execute(bedQuery)
    rows = cur.fetchall()
    # print(type(rows))
    # print(rows[0])
    cur.close()
    conn.close()
    return render(request, 'bed_page.html', {'bedSet': rows})


@login_required
def beddetail(request, device_id):
    try:
        conn = pymysql.connect("114.55.6.251", "root", "ad016dbbab", "softide_cloud2",charset="utf8")
        print("Successful connection to db softide_cloud2")
    except:
        print("Failed to connect to db softide_cloud2")
        return HttpResponseRedirect(reverse('homepage'))
    cur = conn.cursor()
    bed_detail_query = "SELECT id, device_id, date, clear_duration  FROM sc_sleep_quality_day_2018 WHERE device_id = (%s);"
    cur.execute(bed_detail_query, (device_id,))
    rows = cur.fetchall()
    print(rows)
    cur.close()
    conn.close()
    return render(request, 'bed_detail_page.html', {'bedInfo': rows})



@login_required
def addpeople(request):
    curUser = get_object_or_404(User, pk=request.user.id)
    if curUser.username == "jiaxingyiyuan":
        return add_patient(request)
    elif curUser.username == "ronghua":
        return add_old_people(request)
        pass


def add_old_people(request):
    return HttpResponseRedirect(reverse('homepage'))


def add_patient(request):
    form = PatientForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatient = Patient.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            DMGENDER=form.cleaned_data['DMGENDER'],
            DMAGE=form.cleaned_data['DMAGE'],
            DMHEIGHT=form.cleaned_data['DMHEIGHT'],
            DMWEIGHT=form.cleaned_data['DMWEIGHT'],
            DMSTDTC=form.cleaned_data['DMSTDTC'],
            DMENDTC=form.cleaned_data['DMENDTC'],
        )
        newPatient.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '病人'})


@login_required
def addmedhistory(request):
    form = PatientMHForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatientMH = PatientMH.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            MHDATE=form.cleaned_data['MHDATE'],
            MHPAST=form.cleaned_data['MHPAST'],
            MHPERSONAL=form.cleaned_data['MHPERSONAL'],
            MHFAMILY=form.cleaned_data['MHFAMILY'],
            MHSSTATE=form.cleaned_data['MHSSTATE'],
            MHESTATE=form.cleaned_data['MHESTATE'],
        )
        newPatientMH.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientMHForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '病史'})


@login_required
def adddaydiag(request):
    form = PatientTEForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatientTE = PatientTE.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            TETEST=form.cleaned_data['TETEST'],
            TERESULT=form.cleaned_data['TERESULT'],
            TEDATE=form.cleaned_data['TEDATE'],
            TETORESULT=form.cleaned_data['TETORESULT'],
        )
        newPatientTE.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientTEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '每日问诊'})


@login_required
def addradreport(request):
    form = PatientLBForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatientLB = PatientLB.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            LBDATE=form.cleaned_data['LBDATE'],
            LBCATE=form.cleaned_data['LBCATE'],
            LBSUCATE=form.cleaned_data['LBSUCATE'],
            LBTEST=form.cleaned_data['LBTEST'],
            LBRESULT=form.cleaned_data['LBRESULT'],
        )
        newPatientLB.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientLBForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '化验放射检验报告'})


@login_required
def adddrughistory(request):
    form = PatientEXForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatientEX = PatientEX.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            EXDOSE=form.cleaned_data['EXDOSE'],
            EXDATE=form.cleaned_data['EXDATE'],
        )
        newPatientEX.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientEXForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '用药记录'})


@login_required
def addsurghistory(request):
    form = PatientPRForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatientPR = PatientPR.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            PRFIGE=form.cleaned_data['PRFIGE'],
            PRCATE=form.cleaned_data['PRCATE'],
            PRDATE=form.cleaned_data['PRDATE'],
        )
        newPatientPR.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientPRForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '用药记录'})


@login_required
def addbodystatus(request):
    form = PatientPEForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        newPatientPE = PatientPE.objects.create(
            BEDID=form.cleaned_data['BEDID'],
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            PETEST=form.cleaned_data['PETEST'],
            PERESULT=form.cleaned_data['PERESULT'],
            PEDATE=form.cleaned_data['PEDATE'],
        )
        newPatientPE.save()
        return HttpResponseRedirect(reverse('homepage'))
    else:
        newForm = PatientPEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'msg': '体格检验'})
