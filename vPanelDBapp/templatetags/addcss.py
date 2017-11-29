from django import template
from vPanelDBapp.models import PermissionGroup

register = template.Library()

@register.filter(name='has_group')
def has_group(user, permissiongroup):
    groups = [item.strip() for item in permissiongroup.split(",")]  # remove whitespace
    if str(user.permissiongroup) in groups:
        return True