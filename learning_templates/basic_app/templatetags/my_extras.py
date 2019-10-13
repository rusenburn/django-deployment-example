from django import template

register = template.Library()


@register.filter(name="cutting")
def cut(value,arg):
    """
    This cuts out all value of "arg" from string
    """

    return value.replace(arg,'')


# register.filter('cut',cut)
