from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions

from widgets import Link


class ObjectDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        cancel_url = kwargs.pop('cancel_url')
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FormActions(
                Submit('delete', 'Delete', css_class="btn-danger"),
                Link('Cancel', href=cancel_url, css_class="btn")
            )
        )
        super(ObjectDeleteForm, self).__init__(*args, **kwargs)

