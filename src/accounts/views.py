import json

from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.http import is_safe_url
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from accounts.forms import RegisterForm, ProfileEditForm
from accounts.models import UserProfile
# Create your views here.

def register(request):
    if not request.user.is_authenticated():
        
        redirect_to = request.REQUEST.get('next', '')

        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_data = request.POST.copy()
                user = form.save()
                user_profile = UserProfile(user=user)
                user_profile.save()
                email = user.email
                username = user.username
                password = new_data['password']
                try:
                    email_subject = _('Welcome to Baiol')
                    full_name = user.profile.get_display_name()
                    message = _('Dear') + ' ' + full_name + \
                        ',\n\n' + _('Thanks for signing up at Baiol') + \
                        '\n' + _('Remember your login credentials:') + \
                        '\n\n' + _('User name: ') + username + '\n' + \
                        _('Password: ') + password + '\n\n' + \
                        _('Sincerely Baiol')
                    send_mail(
                        email_subject, message, 'Baiol <contact@wmtools.me>',
                        [email], fail_silently=False
                    )
                except:
                    pass
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)

                if redirect_to:
                    if is_safe_url(url=redirect_to, host=request.get_host()):
                        return HttpResponseRedirect(redirect_to)
                return HttpResponseRedirect(reverse('main:home', args=[]))
        else:
            form = RegisterForm()
        form_meta = {'title': _('Sign up'), 'button': _('Sign up')}
        page = {'title': _('Sign up'), 'description': _(
            'Buy Easy, buy now.')}
        context = {'form': form,
                   'form_meta': form_meta,
                   'page': page,
                   'next': reverse('main:home', args=[])
        }

        return render(request, 'accounts/register.html', context)
    else:
        return HttpResponseForbidden()
    
@login_required
def profile(request):
    user = request.user
    
    breadcrumbs = [
        (_('Home'), reverse('main:home')),
        (_('Profile settings'), '')
    ]
    page = {
        'code': 'profile_settings',
        'title': _('%(full_name)s') % {
            'full_name': user.profile.get_display_name()
        }
    }

    return render(request, 'accounts/profile.html', locals())

@login_required
def profile_edit(request):
    user = request.user
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()

            messages.add_message(request, messages.SUCCESS, _(
                '<strong>Success!</strong> You have updated your profile.'))
            return redirect(reverse('accounts:profile_edit', args=[]))
    else:
        form = ProfileEditForm(instance=user)

    breadcrumbs = [
        (_('Home'), reverse('main:home')),
        (_('Profile settings'), reverse('accounts:profile', args=[])),
        (_('Edit Profile'), '')
    ]
    page = {'code': 'profile_edit', 'title': _('Edit profile'), }
    form_meta = {
        'title': _('Edit profile'),
        'button': _('Save'),
        'action': '',
        'form_class': 'col-lg-8 col-lg-offset-2',
        'header_class': 'header-form-profile'
    }
    form.form_meta = form_meta
    context = {'form': form, 'page': page, 'breadcrumbs': breadcrumbs}
    return render(request, 'accounts/base_profile_edit.html', context)
