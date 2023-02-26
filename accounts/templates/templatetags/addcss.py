from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field,attributes):
    className = attributes
    return field.as_widget(attrs={"class":className})