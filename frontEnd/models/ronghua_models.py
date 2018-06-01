from django.db import models
# Create your models here.


class RonghuaBed(models.Model):
    bed_ID = models.IntegerField(primary_key=True, verbose_name='床号')

    class Meta:
        db_table = "ronghua_bed"
        verbose_name_plural = '荣华病床(ronghua_bed)'

    def __str__(self):
        return str(self.pk)+'号床'


class DM_Ronghua(models.Model):
    BEDID = models.ForeignKey(RonghuaBed, verbose_name='床号', on_delete=models.CASCADE)
    Gender_Choices = {
        ('M', '男性'),
        ('F', '女性'),
    }
    SUBJECTID = models.IntegerField(verbose_name='病号')
    DMGENDER = models.CharField(max_length=100, choices=Gender_Choices, verbose_name='性别', blank=True, null=True)
    DMAGE = models.IntegerField(verbose_name='年龄', blank=True, null=True)
    DMHEIGHT = models.IntegerField(verbose_name='身高', help_text='(cm)', blank=True, null=True)
    DMWEIGHT = models.FloatField(verbose_name='体重', help_text='(kg)', blank=True, null=True)
    DMSTDTC = models.DateField(verbose_name='入院日期', blank=True, null=True)
    DMENDTC = models.DateField(verbose_name='出院日期', blank=True, null=True)
    DMENTDIAG = models.CharField(max_length=200, verbose_name='入院诊断', blank=True, null=True)

    class Meta:
        db_table = "ronghua_demographic"
        verbose_name_plural = '荣华病人基本信息(ronghua_demographic)'
        unique_together = ['BEDID', 'SUBJECTID']

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class EX_Ronghua(models.Model):
    BEDID = models.ForeignKey(RonghuaBed, verbose_name='床号', on_delete=models.CASCADE)
    SUBJECTID = models.IntegerField(verbose_name='病号')
    EXDOSE = models.CharField(max_length=200, verbose_name='每次用药剂量', blank=True, null=True)
    EXDOSEUNIT = models.CharField(max_length=200, verbose_name='剂量单位', blank=True, null=True)
    EXDOCTYPE = models.CharField(max_length=200, verbose_name='医嘱类型', blank=True, null=True)
    EXDATE = models.DateField(verbose_name='给药日期', blank=True, null=True)

    class Meta:
        db_table = "ronghua_exposure"
        verbose_name_plural = '荣华用药记录(ronghua_exposure)'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class NU_Ronghua(models.Model):
    BEDID = models.ForeignKey(RonghuaBed, verbose_name='床号', on_delete=models.CASCADE)
    SUBJECTID = models.IntegerField(verbose_name='病号')
    NUCATE = models.CharField(max_length=200, verbose_name='护理分类', blank=True, null=True)
    NURESULT = models.CharField(max_length=200, verbose_name='护理结果', blank=True, null=True)
    NUDATE = models.DateField(verbose_name='护理时间', blank=True, null=True)

    class Meta:
        db_table = "ronghua_nursing"
        verbose_name_plural = '荣华护理记录(ronghua_nursing)'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class PE_Ronghua(models.Model):
    BEDID = models.ForeignKey(RonghuaBed, verbose_name='床号', on_delete=models.CASCADE)
    SUBJECTID = models.IntegerField(verbose_name='病号')
    PEOPT = models.BooleanField(verbose_name='是否手术')
    PECATE = models.CharField(max_length=200, verbose_name='检验分类', blank=True, null=True)
    PERESULT = models.CharField(max_length=200, verbose_name='检验结果', blank=True, null=True)
    PEDATE = models.DateField(verbose_name='检验时间', blank=True, null=True)

    class Meta:
        db_table = "ronghua_physical_examination"
        verbose_name_plural = '荣华体检表(ronghua_physical_examination)'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)


class BB_Ronghua(models.Model):
    BEDID = models.ForeignKey(RonghuaBed, verbose_name='床号', on_delete=models.CASCADE)
    SUBJECTID = models.IntegerField(verbose_name='病号')
    BBCATE = models.CharField(max_length=200, verbose_name='检验分类', blank=True, null=True)
    BBRESULT = models.CharField(max_length=200, verbose_name='检验结果', blank=True, null=True)
    BBDATE = models.DateField(verbose_name='检验时间', blank=True, null=True)

    class Meta:
        db_table = "ronghua_baby"
        verbose_name_plural = '荣华婴儿表(ronghua_baby)'

    def __str__(self):
        return str(self.BEDID) + '-' + str(self.SUBJECTID)
