from django.db import models
from adaptor.fields import *
from adaptor.model import CsvModel, CsvDbModel, ImproperlyConfigured,\
    CsvException, CsvDataException, TabularLayout, SkipRow,\
    GroupedCsvModel, CsvFieldDataException


class Account(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TextField()
    address = models.CharField(max_length=500)
    map_long = models.DecimalField(max_digits=11, decimal_places=8, default=0.0)
    map_lat = models.DecimalField(max_digits=11, decimal_places=8, default=0.0)
    is_featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Accounts'


class Loyaltycodes2(models.Model):
    VARIANT_TYPES = (
        ('JDTW & JDTH','JDTW & JDTH'),
        ('Gentleman Jack', 'Gentleman Jack'),
        ('Single Barrel', 'Single Barrels'),
    )
    VOLUME_TYPES = (
        ('700mL','700mL'),
        ('1000mL','1000mL'),
        ('2000mL','2000mL'),
    )
    PREMISE_TYPES = (
        ('On-Premise','On-Premise'),
        ('Off-Premise','Off-Premise'),
    )
    code = models.CharField(max_length=20)
    variant = models.CharField(choices=VARIANT_TYPES,default='JDTW & JDTH',max_length=20)
    volume = models.CharField(choices=VOLUME_TYPES, default='700mL', max_length=10)
    loyalty_point = loyalty_point = models.IntegerField(default=0)
    tag_account = models.ForeignKey(Account,null=True,blank=True)
    premise = models.CharField(choices=PREMISE_TYPES, default='On-Premise', max_length=20)
    # code_validity_start = models.DateField(null=True, blank=True)
    # code_validity_end = models.DateField(null=True, blank=True)
    # status = models.CharField(max_length=20)
    # author = models.CharField(max_length=20)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Loyalty Codes 2'


class CsvLoyalty(CsvDbModel):

    class Meta:
        dbModel = Loyaltycodes2
        delimiter = ";"

class CsvLoyalty2(CsvModel):
    code = CharField()
    variant = CharField()
    volume = CharField()
    loyalty_point = IntegerField()
    tag_account = DjangoModelField(Account)
    premise = CharField()
    # code_validity_start = CharField()
    # code_validity_end = CharField()
    # status = CharField()
    # author = CharField()

    class Meta:
        has_header = True
        delimiter = ";"
        dbModel = Loyaltycodes2