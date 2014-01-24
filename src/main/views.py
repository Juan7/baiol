from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from stores.models import Store

def home(request):
    user = request.user
    #if not user.is_authenticated():
    stores = Store.objects.all()[:10]
    context = {
            'stores' : stores,
        }
    return render(request, 'main/main.html', context)
    '''
    else:
        return HttpResponseRedirect(reverse('projects:main', args=()))
    '''
    