from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Trabajadores,Rubros
from ..Zonas.models import Zonas
from ..Usuarios.models import Usuarios
from django.db import transaction

#ALTA------------------------------------
#Se hereda del UserCreationForm ya que cuenta con todo el tema de validaciones para el create de un usuario
#Formulario de registrar un trabajador
class TrabajadoresForm(UserCreationForm):
    #Campos que son del trabajador y por ende no estan en el usuario
    #Se lo tiene que poner a mano
    Especialidad=forms.CharField(max_length=50)
    Rubro=forms.ModelChoiceField(Rubros.objects.all())
    Certificado=forms.ImageField(required=False)
    zonas=forms.ModelMultipleChoiceField(Zonas.objects.all())
    
    class Meta:
        model=Usuarios
        fields=['first_name','last_name','username','password1','password2','email','phone','address']

    def __init__(self, *args, **kwargs):
        super(TrabajadoresForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name!='Certificado':
                visible.field.widget.attrs['class'] = 'form-control'        
        
#Se redefine el save ya que los unicos datos que se guardan son del modelo que se asigna en el Meta
#Por ende hay que crear un trabajador a mano en este metodo
    @transaction.atomic
    def save(self):
        usuario=super().save(commit=False)
        usuario.Trabajador=True
        usuario.save()
        job = Trabajadores.objects.create(usuario=usuario,       
        especialidad=self.cleaned_data.get('Especialidad'),rubro=self.cleaned_data['Rubro'],
        certificado=self.cleaned_data['Certificado'])
        zone=self.cleaned_data['zonas']
        for z in zone:
            job.zonas.add(z)
        
        job.save()

        return usuario


        
#UPDATE-----------------------------------------
#Se hereda del UserChangeForm ya que cuenta con todo el tema de validaciones para el update de un usuario
#Formulario de editar el perfil de un trabajador
class EditarForm(UserChangeForm):
    #Campos que son del trabajador y por ende no estan en el usuario
    especialidad=forms.CharField(max_length=50)
    rubro=forms.ModelChoiceField(Rubros.objects.all())
    certificado=forms.ImageField(required=False)
    zonas=forms.ModelMultipleChoiceField(Zonas.objects.all())

    class Meta: #Se ocupa el modelo usuario para que django se encargue de las validaciones
        model=Usuarios
        fields=['first_name','last_name','username','email','phone','address']
        

#Se redefine el init para mostrar los datos de la instancia en los campos que no son del modelo usuario
#kwargs['instance'] tiene la instancia del modelo en ese momento, en este caso usuario
#Con la relacion Worker se accede a los datos de los campos del trabajador
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['especialidad'].initial=kwargs['instance'].Worker.especialidad
        self.fields['rubro'].initial=kwargs['instance'].Worker.rubro
        self.fields['certificado'].initial=kwargs['instance'].Worker.certificado
        self.fields['zonas'].initial=kwargs['instance'].Worker.zonas.all()
        for visible in self.visible_fields():
            if visible.name != 'password' and visible.name!='certificado':
                visible.field.widget.attrs['class'] = 'form-control'
        
        

#Se redefine el Save porque lo unico que se guardaria son los campos del usuario y no los del trabajador
    @transaction.atomic
    def save(self):
        usuario=super().save(commit=False)
        usuario.save()
        trabajador=usuario.Worker
        trabajador.especialidad=self.cleaned_data.get('especialidad')
        trabajador.rubro=self.cleaned_data['rubro']
        trabajador.certificado=self.cleaned_data['certificado']
        zone=self.cleaned_data['zonas']
        trabajador.zonas.set(zone)
        trabajador.save()
        return usuario