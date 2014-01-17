from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


def home(request):
    user = request.user
    #if not user.is_authenticated():
    context = {}
    return render(request, 'main/main.html', context)
    '''
    else:
        return HttpResponseRedirect(reverse('projects:main', args=()))
    '''
    