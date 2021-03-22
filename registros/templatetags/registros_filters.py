from django import template
from registros.models import Grupo

register = template.Library()

@register.simple_tag
def get_grupos():
    grupos = Grupo.objects.all
    if grupos:
        return grupos
    return False 