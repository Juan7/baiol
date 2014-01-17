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

# Create your views here.

def register(request, plan_slug):
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
                return HttpResponseRedirect(reverse('home:home', args=[]))
        else:
            form = RegisterForm()
        form_meta = {'title': _('Sign up'), 'button': _('Sign up')}
        page = {'title': _('Sign up'), 'description': _(
            'Buy Easy, buy now.')}
        context = {'form': form,
                   'form_meta': form_meta,
                   'page': page,
                   #'next': reverse('accounts:plan_user', args=[plan_slug])
        }

        return render(request, 'accounts/register.html', context)
    else:
        return HttpResponseForbidden()