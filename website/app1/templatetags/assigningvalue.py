from django import template

register = template.Library()

@register.filter
def assign(value, arg):
    return value.replace(arg, '')