from django import forms
from django.forms import ModelForm
from .models.ronghua_models import *
from .models.yiyuan_models import *


class BedForm(forms.Form):
    bed_ID = forms.IntegerField(label='床号')


class PatientForm(ModelForm):
    in_date = forms.DateField(label="入院日期", widget=forms.DateInput(attrs={'type': 'date'}))
    out_date = forms.DateField(label="出院日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Patient
        fields = ['subject_id', 'gender', 'age', 'height', 'weight']


class PatientMHForm(ModelForm):
    inquiry_date = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientMH
        widgets = {'past_history': forms.TextInput(attrs={'style':'height:30px; width: 700px'}),
                   'personal_history': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'family_history': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'in_symptom': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'out_symptom': forms.TextInput(attrs={'style': 'height:30px; width: 700px'})}
        fields = ['subject_id', 'past_history', 'personal_history', 'family_history', 'in_symptom', 'out_symptom']


class PatientTEForm(ModelForm):
    date = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientTE
        widgets = {'exam_program': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'all_result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'})}
        fields = ['subject_id', 'exam_program', 'result', 'all_result']


class PatientLBForm(ModelForm):
    date = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientLB
        widgets = {'category': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'subcategory': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'exam_program': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),}
        fields = ['subject_id', 'category', 'subcategory', 'exam_program', 'result']


class PatientEXForm(ModelForm):
    date = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientEX
        widgets = {'dose': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),}
        fields = ['subject_id', 'dose']


class PatientPRForm(ModelForm):
    date = forms.DateField(label="手术时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientPR
        fields = ['subject_id', 'is_operated', 'category']


class PatientPEForm(ModelForm):
    date = forms.DateField(label="体格检查日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientPE
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['subject_id', 'category', 'result']


class DM_RonghuaForm(ModelForm):
    in_date = forms.DateField(label="入院日期", widget=forms.DateInput(attrs={'type': 'date'}))
    out_date = forms.DateField(label="出院日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DM_Ronghua
        widgets = {'in_diagnose': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['subject_id', 'gender', 'age', 'height', 'weight', 'in_diagnose']


class EX_RonghuaForm(ModelForm):
    date = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = EX_Ronghua
        fields = ['subject_id', 'dose', 'unit', 'doctor_advice']


class NU_RonghuaForm(ModelForm):
    date = forms.DateField(label="护理时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = NU_Ronghua
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['subject_id', 'category', 'result']


class PE_RonghuaForm(ModelForm):
    date = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PE_Ronghua
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['subject_id', 'is_operated', 'category', 'result']


class BB_RonghuaForm(ModelForm):
    date = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BB_Ronghua
        widgets = {'result': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['subject_id', 'category', 'result']

