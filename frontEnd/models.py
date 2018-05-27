from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Bed(models.Model):
#     bed_name = models.CharField(max_length=100, verbose_name='床名')
#
#     class Meta:
#         verbose_name_plural = '病床'
#
#     def __str__(self):
#         return str(self.pk) + self.bed_name


class Patient(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    Gender_Choices = {
        ('M', '男性'),
        ('F', '女性'),
    }
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    DMGENDER = models.CharField(max_length=100, choices=Gender_Choices, verbose_name='性别', blank=True, null=True)
    DMAGE = models.IntegerField(verbose_name='年龄', blank=True, null=True)
    DMHEIGHT = models.IntegerField(verbose_name='身高', help_text='(cm)', blank=True, null=True)
    DMWEIGHT = models.FloatField(verbose_name='体重', help_text='(kg)', blank=True, null=True)
    DMSTDTC = models.DateField(verbose_name='入院日期', blank=True, null=True)
    DMENDTC = models.DateField(verbose_name='出院日期', blank=True, null=True)

    class Meta:
        verbose_name_plural = '病人基本信息'
        unique_together = ['BEDID', 'SUBJECTID']

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PatientMH(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    MHDATE = models.DateField(verbose_name='问诊时间', blank=True, null=True)
    MHPAST = models.CharField(max_length=200, verbose_name='既往史', blank=True, null=True)
    MHPERSONAL = models.CharField(max_length=200, verbose_name='个人史', blank=True, null=True)
    MHFAMILY = models.CharField(max_length=200, verbose_name='家族史', blank=True, null=True)
    MHSSTATE = models.CharField(max_length=200, verbose_name='现病史（入院病症）', blank=True, null=True)
    MHESTATE = models.CharField(max_length=200, verbose_name='现病史（出院病症）', blank=True, null=True)

    class Meta:
        verbose_name_plural = '病人病史'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PatientTE(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    TETEST = models.CharField(max_length=200, verbose_name='每日检查项目', blank=True, null=True)
    TERESULT = models.CharField(max_length=200, verbose_name='检查结果', blank=True, null=True)
    TEDATE = models.DateField(verbose_name='问诊时间', blank=True, null=True)
    TETORESULT = models.CharField(max_length=200, verbose_name='总问诊结果', blank=True, null=True)

    class Meta:
        verbose_name_plural = '病人每日问诊'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PatientLB(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    LBDATE = models.DateField(verbose_name='检验时间', blank=True, null=True)
    LBCATE = models.CharField(max_length=200, verbose_name='检验分类', blank=True, null=True)
    LBSUCATE = models.CharField(max_length=200, verbose_name='检验子分类', blank=True, null=True)
    LBTEST = models.CharField(max_length=200, verbose_name='检验项目', blank=True, null=True)
    LBRESULT = models.CharField(max_length=200, verbose_name='检验结果', blank=True, null=True)

    class Meta:
        verbose_name_plural = '病人化验放射检验报告'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PatientEX(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    EXDOSE = models.CharField(max_length=200, verbose_name='每次用药剂量')
    EXDATE = models.DateField(verbose_name='给药日期', blank=True, null=True)

    class Meta:
        verbose_name_plural = '病人用药记录'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PatientPR(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    PRFIGE = models.BooleanField(verbose_name='是否手术')
    PRCATE = models.CharField(max_length=200, verbose_name='手术类别', blank=True, null=True)
    PRDATE = models.DateField(verbose_name='手术时间', blank=True, null=True)

    class Meta:
        verbose_name_plural = '病人手术状况'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PatientPE(models.Model):
    # BEDID = models.ForeignKey(Bed, verbose_name='床号', on_delete=models.CASCADE)
    BEDID = models.IntegerField(verbose_name='床号')
    SUBJECTID = models.IntegerField(verbose_name='病号')
    PETEST = models.CharField(max_length=200, verbose_name='体格检查名称')
    PERESULT = models.CharField(max_length=200, verbose_name='体格检查结果')
    PEDATE = models.DateField(verbose_name='体格检查日期')

    class Meta:
        verbose_name_plural = '病人体格检验'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)




