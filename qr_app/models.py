from django.db import models

# Create your models here.

class Report(models.Model):
    #Codigo de identificaciion----------------------------------------------------------------------------
    id_code = models.CharField(primary_key=True, max_length=8, null=False, verbose_name='id_code')
    
    #Personal Info----------------------------------------------------------------------------------------
    name = models.CharField(max_length=80,blank=True, null=True, verbose_name='Nombre')
    age = models.SmallIntegerField(null=True, blank=True, verbose_name='Edad')
    direccion = models.CharField(max_length=80,blank=True, null=True, verbose_name='Dirección')
    nss = models.CharField(max_length=80,blank=True, null=True, verbose_name='NSS')
    curp = models.CharField(max_length=80,blank=True, null=True, verbose_name='Curp')
    number_1 = models.BigIntegerField(null=True, blank=True, verbose_name='Numero 1')
    number_2 = models.BigIntegerField(null=True, blank=True, verbose_name='Numero 2')
    number_3 = models.BigIntegerField(null=True, blank=True, verbose_name='Numero 3')
    number_4 = models.BigIntegerField(null=True, blank=True, verbose_name='Numero 4')
    email = models.CharField(max_length=80, blank=True, null=True, verbose_name='Correo electrónico') 
    email_2 = models.CharField(max_length=80, blank=True, null=True, verbose_name='Correo electrónico 2')

    #Medical info------------------------------------------------------------------------------------------
    blood = models.CharField(max_length=80,blank=True, null=True, verbose_name='Tipo de sangre')
    allergies_1 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Alergia 1')
    allergies_2 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Alergia 2')
    allergies_3 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Alergia 3')    
    diabetes = models.CharField(max_length=80,blank=True, null=True, verbose_name='Diabetes')
    med_1 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Medicamento 1')
    med_2 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Medicamento 2')
    med_3 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Medicamento 3')
    med_4 = models.CharField(max_length=80,blank=True, null=True, verbose_name='Medicamento 4')

    #Extra info--------------------------------------------------------------------------------------------
    extra_info = models.CharField(max_length=500, blank=True, null=True, verbose_name='Información importante que desea agregar')
       

    

