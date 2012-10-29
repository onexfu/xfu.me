from django import forms
from django.contrib.auth import authenticate

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from crispy_forms.bootstrap import FormActions


class LoginButton(object):
    group_wrap = '<div class="control-group">%s</div>'
    control_wrap = '<div class="controls">%s</div>'
    btn = '<button type="submit" class="btn">Login</button>'

    @classmethod
    def render(self):
        temp = self.control_wrap % self.btn
        return self.group_wrap % temp



class AccountField(forms.EmailField):
    default_error_messages = {
        'required': 'Enter your email address.',
        'invalid': 'Enter a valid email address.',
    }


class PasswordField(forms.CharField):
    default_error_messages = {
        'required': 'Enter your password.',
    }


class LoginForm(forms.Form):
    """ 
    This form authenticates email and password,
    and check if user is staff
    """
    email = AccountField()
    password = PasswordField(widget=forms.PasswordInput())

    error_messages = {
        'invalid_login': "The email or password you entered is incorrect.",
    }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)
        
        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if not self.user_cache:
                raise forms.ValidationError(self.error_messages['invalid_login'])
        return password

    def get_user(self):
        return self.user_cache

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        HTML('<legend>Sign in</legend>'),
        Field('email', css_class='input-large'),
        Field('password', css_class='input-large'),
        HTML(LoginButton.render()),
    )




