from django import forms
from django.forms import ModelForm
from .models.ronghua_models import *
from .models.yiyuan_models import *


class BedForm(forms.Form):
    bed_ID = forms.IntegerField(label='床号')


class PatientForm(ModelForm):
    DMSTDTC = forms.DateField(label="入院日期", widget=forms.DateInput(attrs={'type': 'date'}))
    DMENDTC = forms.DateField(label="出院日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Patient
        fields = ['SUBJECTID', 'DMGENDER', 'DMAGE', 'DMHEIGHT', 'DMWEIGHT']


class PatientMHForm(ModelForm):
    MHDATE = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientMH
        widgets = {'MHPAST': forms.TextInput(attrs={'style':'height:30px; width: 700px'}),
                   'MHPERSONAL': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'MHFAMILY': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'MHSSTATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'MHESTATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'})}
        fields = ['SUBJECTID', 'MHPAST', 'MHPERSONAL', 'MHFAMILY', 'MHSSTATE', 'MHESTATE']


class PatientTEForm(ModelForm):
    TEDATE = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientTE
        widgets = {'TETEST': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'TERESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'TETORESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'})}
        fields = ['SUBJECTID', 'TETEST', 'TERESULT', 'TETORESULT']


class PatientLBForm(ModelForm):
    LBDATE = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientLB
        widgets = {'LBCATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'LBSUCATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'LBTEST': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'LBRESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),}
        fields = ['SUBJECTID', 'LBCATE', 'LBSUCATE', 'LBTEST', 'LBRESULT']


class PatientEXForm(ModelForm):
    EXDATE = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientEX
        widgets = {'EXDOSE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),}
        fields = ['SUBJECTID', 'EXDOSE']


class PatientPRForm(ModelForm):
    PRDATE = forms.DateField(label="手术时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientPR
        fields = ['SUBJECTID', 'PRFIGE', 'PRCATE']


class PatientPEForm(ModelForm):
    PEDATE = forms.DateField(label="体格检查日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientPE
        widgets = {'PERESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['SUBJECTID', 'PETEST', 'PERESULT']


class DM_RonghuaForm(ModelForm):
    DMSTDTC = forms.DateField(label="入院日期", widget=forms.DateInput(attrs={'type': 'date'}))
    DMENDTC = forms.DateField(label="出院日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DM_Ronghua
        widgets = {'DMENTDIAG': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['SUBJECTID', 'DMGENDER', 'DMAGE', 'DMHEIGHT', 'DMWEIGHT', 'DMENTDIAG']


class EX_RonghuaForm(ModelForm):
    EXDATE = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = EX_Ronghua
        fields = ['SUBJECTID', 'EXDOSE', 'EXDOSEUNIT', 'EXDOCTYPE']


class NU_RonghuaForm(ModelForm):
    NUDATE = forms.DateField(label="护理时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = NU_Ronghua
        widgets = {'NURESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['SUBJECTID', 'NUCATE', 'NURESULT']


class PE_RonghuaForm(ModelForm):
    PEDATE = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PE_Ronghua
        widgets = {'PERESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['SUBJECTID', 'PEOPT', 'PECATE', 'PERESULT']


class BB_RonghuaForm(ModelForm):
    BBDATE = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BB_Ronghua
        widgets = {'BBRESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['SUBJECTID', 'BBCATE', 'BBRESULT']

