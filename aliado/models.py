# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoAliado (models.Model):
    nombre = models.CharField(max_length=120)
    abreviatura = models.CharField(max_length=20, null=True, blank=True)

    def  __unicode__(self):
        return u'%s' % (self.nombre)


class RubroInversionEduca (models.Model):
    nombre = models.CharField(max_length=120)
    abreviatura = models.CharField(max_length=20, null=True, blank=True)

    def  __unicode__(self):
        return u'%s, %s' % (self.nombre)

class OpcionRubroEduc(models.Model):
    nombre = models.CharField(max_length=120)
    rubro = models.ForeignKey(RubroInversionEduca)
    ejemplo = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__ (self):
        return u'%s, %s, %s' %(self.nombre, self.rubro, self.ejemplo)

class RubroEmpresa(models.Model):
    nombre = models.CharField(max_length=120)
    abreviatura = models.CharField(max_length=20, null=True, blank=True)

    def  __unicode__(self):
        return u'%s' % (self.nombre)

class Departamento(models.Model):
    codigo = models.CharField(max_length=2, unique=True, help_text=u'Código Oficial del Departamento')
    nombre = models.CharField(max_length=128, unique=True, help_text='Nombre del Departamento')
        
    def __unicode__(self):
        return u'%s' % (self.nombre)

    #para el admin
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Municipio(models.Model):
    codigo = models.CharField(max_length=2, help_text=u'Código Oficial del municipio en el departamento')
    nombre = models.CharField(max_length=128, help_text='Nombre del Municipio')
    departamento = models.ForeignKey(Departamento, help_text='Departamento en el cual se encuentra ubicado')

    def natural_key(self):
        return u'%s | %s' % (self.codigo,self.nombre)
        
    def __unicode__(self):
        if (len(str(self.codigo)) < 2):
            codigo = '0' + str(self.codigo)
        else:
            codigo = str(self.codigo)

        return u'' + codigo + ' | ' + self.nombre

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        unique_together = (("codigo", "departamento"),)


class Aldea(models.Model):
    codigo = models.CharField(max_length=3, help_text=u'Código Oficial de la aldea')
    nombre = models.CharField(max_length=128, help_text= u'Nombre de la Aldea')
    municipio = models.ForeignKey(Municipio, help_text=u'Municipio donde se encuentra ubicada la aldea')

    def natural_key(self):
        return u'%s | %s' % (self.codigo,self.nombre)
        
    def __unicode__(self):
        if (len(str(self.codigo)) < 2):
            codigo = '00' + str(self.codigo)
        else:
            if (len(str(self.codigo)) < 3):
                codigo = '0' + str(self.codigo)
            else:
                codigo = str(self.codigo)

        return u'%s | %s ' % (codigo,self.nombre)

    class Meta:
        verbose_name = 'Aldea'
        verbose_name_plural = 'Aldeas'
        #unique_together = (("codigo", "municipio"),)



def url(obj, filename):
        ruta = "documentos/%s/%s"%(obj.usuario_creador, obj.logo)
        return ruta

class Aliado (models.Model):
    nombre_comercial = models.CharField(max_length=150, null=True, blank=True)
    
    razon_social = models.CharField(max_length=150, null=True, blank=True)
    rtn_aliado = models.CharField(unique = True, null=True, blank=True, max_length=14)
    rubro_aliado = models.ForeignKey(RubroEmpresa, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(null=True, blank=True, max_length = 8)
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, null=True, blank=True)
    aldea = models.ForeignKey(Aldea, null=True, blank=True)
    logo =  models.ImageField(upload_to="url", help_text=u'Seleccione el logo de la empresa', verbose_name=u'Logo:',null=True, blank=True )
    tipo_aliado = models.ForeignKey(TipoAliado, null=True, blank=True)
    rsc_rse = models.BooleanField(default=False) #True == RSC
    rtn_fundacion = models.CharField(null=True, blank=True, max_length=14)
    nombre_fundacion = models.CharField(max_length=150, null=True, blank=True)
    direccion_fundacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_creador = models.ForeignKey(User, related_name='persona_creador')
    usuario_modifico = models.ForeignKey(User, related_name='persona_modificador')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __unicode__ (self):
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s, %s' %(self.razon_social, self.rtn_aliado, 
            self.rubro_aliado, self.departamento, self.municipio, self.aldea, self.tipo_aliado, self.rsc_rse, 
            self.rtn_fundacion, self.nombre_fundacion) 

TITULO_DIRECTIVA = (
    (1, u'ING.'), 
    (2, u'LIC.'),
    (3, u'PHD.'),
    (4, u'MSC.'), 
    (5, u'SRA.' ),
    (6, u'SR.'),

)

class DirectivaAliado(models.Model):
    aliado = models.ForeignKey(Aliado, related_name = 'aliado_directivaaliado')
    titulo = models.CharField(choices =TITULO_DIRECTIVA, max_length=7)
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length= 200)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField(null=True, blank=True)
    celular = models.CharField(null=True, blank=True, max_length=14)
    contacto_rsc_rse = models.BooleanField(default=False)
    contacto_primario = models.BooleanField(default=True)
    usuario_creador = models.ForeignKey(User, related_name='persona_creo_directiva', null=True, blank=True)
    usuario_modifico = models.ForeignKey(User, related_name='persona_modifico_directiva', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__ (self):
        return u'%s, %s, %s, %s, %s' %(self.aliado, self.nombre, self.cargo, 
            self.contacto_rsc_rse, self.contacto_primario)

class Periodo (models.Model):
    aliado = models.ForeignKey(Aliado, related_name = 'aliado_periodo')
    periodo = models.IntegerField()
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_final = models.DateField( )
    presupuesto_minimo = models.DecimalField(max_digits=20, decimal_places=2)
    presupuesto_maximo = models.DecimalField(max_digits=20, decimal_places=2)
    usuario_creador = models.ForeignKey(User, related_name='persona_creo_periodo', null=True, blank=True)
    usuario_modifico = models.ForeignKey(User, related_name='persona_modifico_periodo', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__ (self):
        return u'%s, %s, %s, %s, %s, %s' %(self.aliado, self.periodo, self.fecha_inicio, 
            self.fecha_final, self.presupuesto_minimo, self.presupuesto_maximo)

class RubroEducaAliado (models.Model):
    aliado = models.ForeignKey(Aliado, related_name = 'aliado_rubroaliado')
    rubro_inversion_educac = models.ForeignKey(RubroInversionEduca)

    def __unicode__ (self):
        return u'%s, %s' %(self.aliado, self.rubro_inversion_educac)

class PeriodoRubroEduca(models.Model):
    rubro_educ_aliado = models.ForeignKey(RubroEducaAliado)
    periodo = models.ForeignKey(Periodo)
    porcentaje = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self): 
        return u'%s, %s, %s' %(self.rubro_educ_aliado, self.periodo, self.porcentaje)


class UsuariosAliado (models.Model):
    aliado = models.ForeignKey(Aliado, related_name='usuario_aliado')
    usuario = models.ForeignKey(User, related_name = 'usuarioaliado_user')


# AL CREAR USUARIO SI ENCUENTRA EL RTN, GUARDA USUARIO ALIADO, Y LUEGO MANDA AL MENU, SI NO ENCUENTRA EL RTN LO MANDA DE 
#UN SOLO A REGISTRAR EL ALIADO Y HACE EL GUARDADO NORMAL Y AGREGAR EL USUARIO CREADOR A USUARIOS ALIADO, 
#AGREGAR EL GUARDADO D USUARIOSALIADO EN LA VIEW DE REGISTRAR ALIADO







            

