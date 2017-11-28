from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class AuthForm(AuthenticationForm):
    """
        A custom authentication form used in the administration application.
    """
    error_messages = {
        'invalid_login': (
            _("ERROR MESSAGE.")
        ),
    }
    required_css_class = 'required'

def confirm_login_allowed(self, user):
    if not user.is_active or not user.is_staff:
        raise forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={
                'username': self.username_field.verbose_name
            }
        )