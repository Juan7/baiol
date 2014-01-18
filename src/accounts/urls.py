from django.conf.urls import patterns, url
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from accounts.forms import AuthenticationFormEdited, \
    PasswordChangeFormEdited, PasswordResetFormEdited, \
    SetPasswordFormEdited

urlpatterns = patterns('accounts.views',
    url(r'^register/$', 'register',name='register'),
    url(r'^profile/edit/$', 'profile_edit', name='profile_edit'),
    url(r'^profile/$', 'profile',name='profile'),
    
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login',
    {
        'template_name': 'accounts/login.html',
        'authentication_form': AuthenticationFormEdited,
        'extra_context': {
            'page': {
                'title': _('Log in'),
            }
        }
    }, 'login'),
    url(r'^logout/$', 'logout', {'next_page': '/', }, 'logout'),
    url(r'^profile/password/edit/$', 'password_change',
        {
            'template_name': 'accounts/base_profile_edit.html',
            'password_change_form': PasswordChangeFormEdited,
            'post_change_redirect': '/accounts/message/password_change_done/',
            'extra_context': {
                'page': {
                    'code': 'password_edit',
                    'title': _('Change password')
                },
                'breadcrumbs': [
                    (_('Home'), '/'),
                    (_('Profile settings'), '/accounts/profile/'),
                    (_('Change password'), ''),
                ]
            }
        }, 'password_change', ),
    url(r'^profile/password/reset/$', 'password_reset',
        {
            'template_name': 'main/full_page_form_vertical.html',
            'password_reset_form': PasswordResetFormEdited,
            'post_reset_redirect': '/accounts/message/password_reset/',
            'email_template_name': 'accounts/email.html',
            'extra_context': {
                'page': {
                    'title': _('Reset password')
                },
            }
        }, 'password_reset'),
    url(r'^profile/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'password_reset_confirm', {
            'template_name': 'main/full_page_form_vertical.html',
            'set_password_form': SetPasswordFormEdited,
            'post_reset_redirect': '/accounts/message/password_reset_confirm/',
        }, 'password_reset_confirm',),
)