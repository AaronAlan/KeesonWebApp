# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from frontEnd.forms import *
from frontEnd.models import *

# Create your views here.

@login_required
def bedadddetails(request, bed_id):
    return render(request, 'add_bed_details.html', {'bed_id': bed_id})


@login_required
def addpeople(request, bed_id):
    form = PatientForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        try:
            newPatient = Patient.objects.create(
                bed_number=cur_bed,
                subject_id=form.cleaned_data['subject_id'],
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                in_date=form.cleaned_data['in_date'],
                out_date=form.cleaned_data['out_date'],
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
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '病人基本信息'})


def add_old_people(request):
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def addmedhistory(request, bed_id):
    form = PatientMHForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientMH = PatientMH.objects.create(
            bed_number=cur_bed,
            subject_id=form.cleaned_data['subject_id'],
            inquiry_date=form.cleaned_data['inquiry_date'],
            past_history=form.cleaned_data['past_history'],
            personal_history=form.cleaned_data['personal_history'],
            family_history=form.cleaned_data['family_history'],
            in_symptom=form.cleaned_data['in_symptom'],
            out_symptom=form.cleaned_data['out_symptom'],
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
            bed_number=cur_bed,
            subject_id=form.cleaned_data['subject_id'],
            exam_program=form.cleaned_data['exam_program'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
            all_result=form.cleaned_data['all_result'],
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
            bed_number=cur_bed,
            subject_id=form.cleaned_data['subject_id'],
            date=form.cleaned_data['date'],
            category=form.cleaned_data['category'],
            subcategory=form.cleaned_data['subcategory'],
            exam_program=form.cleaned_data['exam_program'],
            result=form.cleaned_data['result'],
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
            bed_number=cur_bed,
            subject_id=form.cleaned_data['subject_id'],
            dose=form.cleaned_data['dose'],
            date=form.cleaned_data['date'],
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
            bed_number=cur_bed,
            subject_id=form.cleaned_data['subject_id'],
            is_operated=form.cleaned_data['is_operated'],
            category=form.cleaned_data['category'],
            date=form.cleaned_data['date'],
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
            bed_number=cur_bed,
            subject_id=form.cleaned_data['subject_id'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newPatientPE.save()
        redirect_url = reverse('bedAddDetails', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PatientPEForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体格检验'})
