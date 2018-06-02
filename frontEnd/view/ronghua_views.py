# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from frontEnd.forms import *
from frontEnd.models import *


@login_required
def bedadddetails(request, bed_id):
    return render(request, 'ronghua_add_bed_details.html', {'bed_id': bed_id})


@login_required
def addpeople(request, bed_id):
    form = DM_RonghuaForm(request.POST)
    latest_patient = DM_Ronghua.objects.filter(bed_number=bed_id).last()
    if request.method == 'POST' and form.is_valid():
        try:
            if form.cleaned_data['in_date'] is not None and form.cleaned_data['out_date'] is not None \
                    and (form.cleaned_data['in_date'] > form.cleaned_data['out_date']):
                raise Exception
            newPatient = DM_Ronghua(bed_number=bed_id, subject_id=form.cleaned_data['subject_id'],
                                    gender=form.cleaned_data['gender'], age=form.cleaned_data['age'],
                                    height=form.cleaned_data['height'], weight=form.cleaned_data['weight'],
                                    in_date=form.cleaned_data['in_date'], out_date=form.cleaned_data['out_date'],
                                    in_diagnose=form.cleaned_data['in_diagnose'])
            if latest_patient is not None and latest_patient.out_date is None \
                    and newPatient.subject_id != latest_patient.subject_id:
                raise Exception
            if DM_Ronghua.objects.filter(bed_number=bed_id, subject_id=newPatient.subject_id).exists():
                print("exist")
                original_patient = DM_Ronghua.objects.get(bed_number=bed_id, subject_id=newPatient.subject_id)
                if original_patient.out_date is not None:
                    raise Exception
                original_patient.gender = newPatient.gender
                original_patient.age = newPatient.age
                original_patient.height = newPatient.height
                original_patient.weight = newPatient.weight
                original_patient.in_date = newPatient.in_date
                original_patient.out_date = newPatient.out_date
                original_patient.in_diagnose = newPatient.in_diagnose
                original_patient.save()
            else:
                newPatient.save()
            redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
            return HttpResponseRedirect(redirect_url)
        except:
            if latest_patient is not None and latest_patient.out_date is None:
                newForm = DM_RonghuaForm(instance=latest_patient)
            else:
                newForm = DM_RonghuaForm()
            return render(request, 'add_new_info.html', {'form': newForm,
                                                         'bed_id': bed_id,
                                                         'msg': '荣华养老院病人基本信息',
                                                         'error': '输入信息有误：不能输入重复的病号信息；出院时间不能早于入院时间; 完善当前病人信息才可继续添加病人'})
    else:
        if latest_patient is not None and latest_patient.out_date is None:
            insuf_form = DM_RonghuaForm(instance=latest_patient)
            return render(request, 'add_new_info.html', {'form': insuf_form,
                                                         'bed_id': bed_id,
                                                         'msg': '荣华养老院病人基本信息',
                                                         'error': '请填写该病床最近病人出院时间，方可添加新入院病人; 您也可以修改当前病人基本信息'})
        else:
            newForm = DM_RonghuaForm()
            return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '荣华养老院病人基本信息'})


@login_required
def adddrughistory(request, bed_id):
    form = EX_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newEX_Ronghua = EX_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            dose=form.cleaned_data['dose'],
            unit=form.cleaned_data['unit'],
            doctor_advice=form.cleaned_data['doctor_advice'],
            date=form.cleaned_data['date'],
        )
        newEX_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = EX_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '用药记录'})


@login_required
def addnurshistory(request, bed_id):
    form = NU_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newNU_Ronghua = NU_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newNU_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = NU_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '护理记录'})


@login_required
def addtemperature(request, bed_id):
    form = PE_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newPE_Ronghua = PE_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            is_operated=form.cleaned_data['is_operated'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newPE_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = PE_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体温表'})


@login_required
def adddbaby(request, bed_id):
    form = BB_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newBB_Ronghua = BB_Ronghua.objects.create(
            bed_number=bed_id,
            subject_id=form.cleaned_data['subject_id'],
            category=form.cleaned_data['category'],
            result=form.cleaned_data['result'],
            date=form.cleaned_data['date'],
        )
        newBB_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = BB_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体温表'})