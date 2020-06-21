from django import forms


class SideBarAdminform(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,
                              label='内容',
                              required=False)
