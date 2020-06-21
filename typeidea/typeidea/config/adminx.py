import xadmin

from xadmin.layout import Row, Fieldset

from .models import Link, SideBar

from .adminforms import SideBarAdminform
from typeidea.adminx import BaseOwnerAdmin


@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    form = SideBarAdminform
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')


# Register your models here.
