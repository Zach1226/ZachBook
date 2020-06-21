import xadmin

from xadmin.layout import Row, Fieldset

from .models import Comment
from .adminforms import CommentAdminform
from typeidea.adminx import BaseOwnerAdmin


@xadmin.sites.register(
    Comment, )
class CommentAdmin(BaseOwnerAdmin):
    form = CommentAdminform
    list_display = ('target', 'owner', 'content', 'website', 'created_time')
    list_display_links = []

    list_filter = [
        'content',
    ]
    searchfields = ['owner', 'created_name', 'target']
    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True
    exclude = ['target']
    form_layout = (
        Fieldset(
            '信息填写',
            Row("owner", "content"),
        ),
        Fieldset(
            '状态修改',
            'status',
        ),
    )
