import re

from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm

#from main.widgets import AvatarWidget
#from accounts.models import UserProfile, Feedback


class RegisterForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
        max_length=30,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(30)
        ]
    )
    email = forms.EmailField(label=_('Email'))
    password = forms.CharField(
        label=_('Password'),
        max_length=50,
        widget=forms.PasswordInput(render_value=False),
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(50)
        ]
    )

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_('This email is already taken.'))

    def clean_username(self):
        if not re.match(r'^[A-Za-z0-9]+$', self.cleaned_data['username']):
            raise forms.ValidationError(
                _('Only alphanumeric values are valid.'))

        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
            raise forms.ValidationError(_('This username is already taken.'))
        except User.DoesNotExist:
            return self.cleaned_data['username']

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'], self.cleaned_data['email'],
            self.cleaned_data['password'])
        user.username = self.cleaned_data['username']
        user.is_active = True
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['username'].label
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['email'].label
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['password'].label
            }
        )


class ProfileEditForm(ModelForm):

    def clean_email(self):
        if self.instance.email != self.cleaned_data['email']:
            try:
                User.objects.get(email__iexact=self.cleaned_data['email'])
            except User.DoesNotExist:
                return self.cleaned_data['email']
            raise forms.ValidationError(_('This email is already taken.'))
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['first_name'].label
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['last_name'].label
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['email'].label
            }
        )

'''
class AvatarEditForm(ModelForm):

    class Meta:
        model = UserProfile
        field = ('avatar',)
        exclude = ('user',)
        widgets = {
            'avatar': AvatarWidget,
        }

'''
class AuthenticationFormEdited(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationFormEdited, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['username'].label
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['password'].label
            }
        )


class PasswordChangeFormEdited(PasswordChangeForm):
    form_meta = {
        'title': _('Change password'),
        'button': _('Save'),
        'action': '',
        'form_class': 'col-md-8 col-md-offset-2',
        'header_class': 'header-form-profile'
    }

    def __init__(self, *args, **kwargs):
        super(PasswordChangeFormEdited, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['old_password'].label
            }
        )
        self.fields['new_password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['new_password1'].label
            }
        )
        self.fields['new_password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['new_password2'].label
            }
        )


class PasswordResetFormEdited(PasswordResetForm):
    form_meta = {
        'title': _('Reset password'),
        'button': _('Reset'),
        'action': '',
        'form_class': 'col-md-8 col-md-offset-2',
        'header_class':
        'header-form-profile'
    }

    def __init__(self, *args, **kwargs):
        super(PasswordResetFormEdited, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['email'].label
            }
        )


class SetPasswordFormEdited(SetPasswordForm):
    form_meta = {
        'title': _('Reset password'),
        'button': _('Reset'),
        'action': '',
        'form_class': 'col-md-8 col-md-offset-2',
        'header_class': 'header-form-profile'
    }

    def __init__(self, *args, **kwargs):
        super(SetPasswordFormEdited, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['new_password1'].label
            }
        )
        self.fields['new_password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['new_password2'].label
            }
        )

'''
class FeedbackAddForm(ModelForm):
    form_meta = {'title': _('Leave feedback'),
                 'button': _('Send'), 'help_collapse': True, }

    class Meta:
        model = Feedback
        fields = ('subject_type', 'subject', 'message', 'url')

    def __init__(self, *args, **kwargs):
        super(FeedbackAddForm, self).__init__(*args, **kwargs)
        self.fields['subject_type'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['subject_type'].label
            }
        )
        self.fields['subject'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['subject'].label
            }
        )
        self.fields['message'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': self.fields['message'].label
            }
        )
        self.fields['url'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': self.fields['url'].label})

        self.fields['subject_type'].help_text = _(
            'Any suggestion, issue or new feature you want to see or be '
            'solved.')
        self.fields['subject'].help_text = _('A small feedback description.')
        self.fields['message'].help_text = _(
            'A bigger description of your feeback.')
        self.fields['url'].help_text = _(
            'Optional. Include an URL if it is the case.')
'''

