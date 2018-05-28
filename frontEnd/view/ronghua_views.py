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
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        try:
            newDM_Ronghua = DM_Ronghua.objects.create(
                BEDID=cur_bed,
                SUBJECTID=form.cleaned_data['SUBJECTID'],
                DMGENDER=form.cleaned_data['DMGENDER'],
                DMAGE=form.cleaned_data['DMAGE'],
                DMHEIGHT=form.cleaned_data['DMHEIGHT'],
                DMWEIGHT=form.cleaned_data['DMWEIGHT'],
                DMSTDTC=form.cleaned_data['DMSTDTC'],
                DMENDTC=form.cleaned_data['DMENDTC'],
                DMENTDIAG=form.cleaned_data['DMENTDIAG'],
            )
            newDM_Ronghua.save()
            redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
            return HttpResponseRedirect(redirect_url)
        except:
            newForm = DM_RonghuaForm()
            return render(request, 'add_new_info.html', {'form': newForm,
                                                         'bed_id': bed_id,
                                                         'msg': '病人',
                                                         'error': '该病人与病床信息已经存在'})
    else:
        newForm = DM_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '荣华养老院病人基本信息'})


@login_required
def adddrughistory(request, bed_id):
    form = EX_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newEX_Ronghua = EX_Ronghua.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            EXDOSE=form.cleaned_data['EXDOSE'],
            EXDOSEUNIT=form.cleaned_data['EXDOSEUNIT'],
            EXDOCTYPE=form.cleaned_data['EXDOCTYPE'],
            EXDATE=form.cleaned_data['EXDATE'],
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
        cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newNU_Ronghua = NU_Ronghua.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            NUCATE=form.cleaned_data['NUCATE'],
            NURESULT=form.cleaned_data['NURESULT'],
            NUDATE=form.cleaned_data['NUDATE'],
        )
        newNU_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = NU_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '护理记录'})


@login_required
def addtemperature(request, bed_id):
    form = BT_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newBT_Ronghua = BT_Ronghua.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            BTFIGE=form.cleaned_data['BTFIGE'],
            BTCATE=form.cleaned_data['BTCATE'],
            BERESULT=form.cleaned_data['BERESULT'],
            BEDATE=form.cleaned_data['BEDATE'],
        )
        newBT_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = BT_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体温表'})


@login_required
def adddbaby(request, bed_id):
    form = BB_RonghuaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        cur_bed = get_object_or_404(RonghuaBed, bed_ID=bed_id)
        newBB_Ronghua = BB_Ronghua.objects.create(
            BEDID=cur_bed,
            SUBJECTID=form.cleaned_data['SUBJECTID'],
            BBCATE=form.cleaned_data['BBCATE'],
            BBRESULT=form.cleaned_data['BBRESULT'],
            BBDATE=form.cleaned_data['BBDATE'],
        )
        newBB_Ronghua.save()
        redirect_url = reverse('bedAddDetailsRonghua', args=[bed_id, ])
        return HttpResponseRedirect(redirect_url)
    else:
        newForm = BB_RonghuaForm()
        return render(request, 'add_new_info.html', {'form': newForm, 'bed_id': bed_id, 'msg': '体温表'})