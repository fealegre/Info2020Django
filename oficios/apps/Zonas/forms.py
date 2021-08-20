from django.forms import ModelForm

class ZonasForm(ModelForm):
     class Meta:
        #model = Zonas
        fields=['nombre','cp']