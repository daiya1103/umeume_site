from django import template

register = template.Library()

@register.simple_tag
def percentage(a, b):
    result = a / b
    result = round(result, 3)
    return result