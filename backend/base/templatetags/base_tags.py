from django import template

register = template.Library()

# Example
# @register.simple_tag
# def multiply(value, arg):
#     return value * arg


@register.simple_tag
def linkurl(url):
    _url = url.split("/", 2)
    return _url


@register.simple_tag
def menu(user):
    from django.contrib.auth.models import User
    from base.models import Menu

    try:
        _user = User.objects.get(pk=user)

        if _user.is_active:
            # if _user.is_staff:
            #     return Menu.objects.filter(admin=False, support=True)
            # elif _user.is_superuser:
            #     return Menu.objects.filter(admin=True, support=True)
            
            # return Menu.objects.filter(admin=False, support=False)
            return Menu.objects.all()
    except:
        return [dict(name="TESTE", icon="teste"),]


@register.simple_tag
def get_item(value, field_name=None):

    return value
