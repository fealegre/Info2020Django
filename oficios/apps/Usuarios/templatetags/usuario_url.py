from django import template

register = template.Library()

#Devuelve la url correspondiente
@register.filter(name='ObtenerUrl')
def ObtenerUrl(value,destino):
    if(value.Trabajador):
        return 'Trabajadores:'+destino
    return 'Stalkers:'+destino