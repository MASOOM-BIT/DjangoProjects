from django import template
register = template.Library()

@register.filter(name='custLower')
def custLower(value):
    result = value[:3].lower()
    return result

@register.filter(name='custAppend')
def custAppend(value, arg):
    return str(arg) + value

