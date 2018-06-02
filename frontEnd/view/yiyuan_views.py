# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from frontEnd.forms import *
from frontEnd.models import *
from datetime import datetime
# Create your views here.

@login_required
def bedadddetails(request, bed_id):
    return render(request, 'add_bed_details.html', {'bed_id': bed_id})


@login_required
def addpeople(request, bed_id):
    form = PatientForm(request.POST)
    latest_patient = Patient.objects.filter(bed_number=bed_id).last()
    # 用户提交表单：1，当前未出院病人信息（修改或添加）
    #             2，前一病人已出院，添加新病人
    if request.method == 'POST' and form.is_valid():
        try:
            # 入院出院时间必须有效
            if form.cleaned_data['in_date'] is not None and form.cleaned_data['out_date'] is not None \
                    and (form.cleaned_data['in_date'] > form.cleaned_data['out_date']):
                raise Exception
            newPatient = Patient(bed_number=bed_id, subject_id=form.cleaned_data['subject_id'],
                                 gender=form.cleaned_data['gender'], age=form.cleaned_data['age'],
                                 height=form.cleaned_data['height'], weight=form.cleaned_data['weight'],
                                 in_date=form.cleaned_data['in_date'], out_date=form.cleaned_data['out_date'],
                                 )
            # 上一病人必须出院才能添加新病人，否则异常报错
            if latest_patient is not None and latest_patient.out_date is None \
                    and newPatient.subject_id != latest_patient.subject_id:
                raise Exception
            # 提交病人信息已经存在：1，已经出院，异常报错
            #                   2，还未出院，修改或添加信息
            if Patient.objects.filter(bed_number=bed_id, subject_id=newPatient.subject_id).exists():
                print("exist")
                original_patient = Patient.objects.get(bed_number=bed_id, subject_id=newPatient.subject_id)
                if original_patient.out_date is not None:
                    raise Exception
                original_patient.gender = newPatient.gender
                original_patient.age = newPatient.age
                original_patient.height = newPatient.height
                original_patient.weight = newPatient.weight
                original_patient.in_date = newPatient.in_date
                original_patient.out_date = newPatient.out_date
                original_patient.save()
            # 提交新病人信息并保存
            else:
                newPatient.save()
            redirect_url = reverse('bedAddDetails', args=[bed_id, ])
            return HttpResponseRedirect(redirect_url)
        except:
            if latest_patient is not None and latest_patient.out_date is None:
                newForm = PatientForm(instance=latest_patient)
            else:
                newForm = PatientForm()
            return render(request, 'add_new_info.html', {'form': newForm,
                                                         'bed_id': bed_id,
                                                         'msg': '病人基本信息',
                                                         'error': '输入信息有误：不能输入重复的病号信息；出院时间不能早于入院时间; 完善当前病人信息才可继续添加病人'})
    # method = "GET"： 1，当前病人还未出院，渲染旧表单
    #                  2，当前病人已出院，渲染新表单
    else:
        if latest_patient is not None and latest_patient.out_date is None:
            insuf_form = PatientForm(instance=latest_patient)
            return render(request, 'add_new_info.html', {'form': insuf_form,
                                                         'bed_id': bed_id,
                                                         'msg': '病人基本信息',
                                                         'error': '请填写该病床最近病人出院时间，方可添加新入院病人; 您也可以修改当前病人基本信息'})
        else:
            newForm = PatientForm()
            return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '病人基本信息'})


def add_old_people(request):
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def addmedhistory(request, bed_id):
    form = PatientMHForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientMH = PatientMH.objects.create(
            bed_number=bed_id,
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
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientTE = PatientTE.objects.create(
            bed_number=bed_id,
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
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientLB = PatientLB.objects.create(
            bed_number=bed_id,
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
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientEX = PatientEX.objects.create(
            bed_number=bed_id,
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
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientPR = PatientPR.objects.create(
            bed_number=bed_id,
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
        # cur_bed = get_object_or_404(PatientBed, bed_ID=bed_id)
        newPatientPE = PatientPE.objects.create(
            bed_number=bed_id,
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
