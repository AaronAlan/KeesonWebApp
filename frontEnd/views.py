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
    cur_user = get_object_or_404(User, pk=request.user.id)
    if cur_user.username == "jiaxingyiyuan":
        form = PatientBedForm(request.POST)
        bed_exist = False
        if request.method == 'POST' and form.is_valid():
            new_bed, created = PatientBed.objects.get_or_create(bed_ID=form.cleaned_data['bed_ID'])
        new_form = PatientBedForm()
        bed_set = PatientBed.objects.all().order_by('bed_ID')
        return render(request, 'yiyuan_homepage.html', {'form': new_form, 'bed_set': bed_set, 'bed_exist': bed_exist})
    elif cur_user.username == "ronghua":
        return render(request, 'ronghua_homepage.html')


@login_required
def bedadddetails(request, bed_id):
    return render(request, 'add_bed_details.html', {'bed_id': bed_id})


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
def addpeople(request, bed_id):
    curUser = get_object_or_404(User, pk=request.user.id)
    if curUser.username == "jiaxingyiyuan":
        return add_patient(request, bed_id)
    elif curUser.username == "ronghua":
        return add_old_people(request, bed_id)
        pass


def add_old_people(request):
    return HttpResponseRedirect(reverse('homepage'))


def add_patient(request, bed_id):
    form = PatientForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        try:
            newPatient = Patient.objects.create(
                BEDID=cur_bed,
                SUBJECTID=form.cleaned_data['SUBJECTID'],
                DMGENDER=form.cleaned_data['DMGENDER'],
                DMAGE=form.cleaned_data['DMAGE'],
                DMHEIGHT=form.cleaned_data['DMHEIGHT'],
                DMWEIGHT=form.cleaned_data['DMWEIGHT'],
                DMSTDTC=form.cleaned_data['DMSTDTC'],
                DMENDTC=form.cleaned_data['DMENDTC'],
            )
            newPatient.save()
            redirect_url = reverse('bedAddDetails', args=[bed_id, ])
            return HttpResponseRedirect(redirect_url)
        except:
            newForm = PatientForm()
            return render(request, 'add_new_info.html', {'form': newForm,
                                                         'bed_id': bed_id,
                                                         'msg': '病人',
                                                         'error': '该病人与病床信息已经存在'})
    else:
        newForm = PatientForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '病人'})


@login_required
def addmedhistory(request, bed_id):
    form = PatientMHForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientMH = PatientMH.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            MHDATE=form.cleaned_data['MHDATE'],
            MHPAST=form.cleaned_data['MHPAST'],
            MHPERSONAL=form.cleaned_data['MHPERSONAL'],
            MHFAMILY=form.cleaned_data['MHFAMILY'],
            MHSSTATE=form.cleaned_data['MHSSTATE'],
            MHESTATE=form.cleaned_data['MHESTATE'],
        )
        newPatientMH.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientMHForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '病史'})


@login_required
def adddaydiag(request, bed_id):
    form = PatientTEForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientTE = PatientTE.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            TETEST=form.cleaned_data['TETEST'],
            TERESULT=form.cleaned_data['TERESULT'],
            TEDATE=form.cleaned_data['TEDATE'],
            TETORESULT=form.cleaned_data['TETORESULT'],
        )
        newPatientTE.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientTEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '每日问诊'})


@login_required
def addradreport(request, bed_id):
    form = PatientLBForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientLB = PatientLB.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            LBDATE=form.cleaned_data['LBDATE'],
            LBCATE=form.cleaned_data['LBCATE'],
            LBSUCATE=form.cleaned_data['LBSUCATE'],
            LBTEST=form.cleaned_data['LBTEST'],
            LBRESULT=form.cleaned_data['LBRESULT'],
        )
        newPatientLB.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientLBForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '化验放射检验报告'})


@login_required
def adddrughistory(request, bed_id):
    form = PatientEXForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientEX = PatientEX.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            EXDOSE=form.cleaned_data['EXDOSE'],
            EXDATE=form.cleaned_data['EXDATE'],
        )
        newPatientEX.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientEXForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '用药记录'})


@login_required
def addsurghistory(request, bed_id):
    form = PatientPRForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientPR = PatientPR.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            PRFIGE=form.cleaned_data['PRFIGE'],
            PRCATE=form.cleaned_data['PRCATE'],
            PRDATE=form.cleaned_data['PRDATE'],
        )
        newPatientPR.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientPRForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '用药记录'})


@login_required
def addbodystatus(request, bed_id):
    form = PatientPEForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientPE = PatientPE.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            PETEST=form.cleaned_data['PETEST'],
            PERESULT=form.cleaned_data['PERESULT'],
            PEDATE=form.cleaned_data['PEDATE'],
        )
        newPatientPE.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientPEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体格检验'})
