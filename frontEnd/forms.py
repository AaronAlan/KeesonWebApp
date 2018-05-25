from django import forms
from django.forms import ModelForm
from .models import *


# class PersonForm(forms.Form):
#     name = forms.CharField(label="请输入被搜索人的姓名")
#     SUBJECTID = forms.IntegerField(label="请输入被搜索人的病号")
# class BedForm(ModelForm):
#     class Meta:
#         model = Bed
#         fields = '__all__'


class PatientForm(ModelForm):
    DMSTDTC = forms.DateField(label="入院日期", widget=forms.DateInput(attrs={'type': 'date'}))
    DMENDTC = forms.DateField(label="出院日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Patient
        fields = ['BEDID', 'SUBJECTID', 'DMGENDER', 'DMAGE', 'DMHEIGHT', 'DMWEIGHT']


class PatientMHForm(ModelForm):
    MHDATE = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientMH
        widgets = {'MHPAST': forms.TextInput(attrs={'style':'height:30px; width: 700px'}),
                   'MHPERSONAL': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'MHFAMILY': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'MHSSTATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'MHESTATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'})}
        fields = ['BEDID', 'SUBJECTID', 'MHPAST', 'MHPERSONAL', 'MHFAMILY', 'MHSSTATE', 'MHESTATE']


class PatientTEForm(ModelForm):
    TEDATE = forms.DateField(label="问诊时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientTE
        widgets = {'TETEST': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'TERESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'TETORESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'})}
        fields = ['BEDID', 'SUBJECTID', 'TETEST', 'TERESULT', 'TETORESULT']


class PatientLBForm(ModelForm):
    LBDATE = forms.DateField(label="检验时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientLB
        widgets = {'LBCATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'LBSUCATE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'LBTEST': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),
                   'LBRESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),}
        fields = ['BEDID', 'SUBJECTID', 'LBCATE', 'LBSUCATE', 'LBTEST', 'LBRESULT']


class PatientEXForm(ModelForm):
    EXDATE = forms.DateField(label="给药日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientEX
        widgets = {'EXDOSE': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}),}
        fields = ['BEDID', 'SUBJECTID', 'EXDOSE']


class PatientPRForm(ModelForm):
    PRDATE = forms.DateField(label="手术时间", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientPR
        fields = ['BEDID', 'SUBJECTID', 'PRFIGE', 'PRCATE']


class PatientPEForm(ModelForm):
    PEDATE = forms.DateField(label="体格检查日期", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientPE
        widgets = {'PERESULT': forms.TextInput(attrs={'style': 'height:30px; width: 700px'}), }
        fields = ['BEDID', 'SUBJECTID', 'PETEST', 'PERESULT']