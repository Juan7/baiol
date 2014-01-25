from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from stores.models import Store
from products.models import Product, Category, Department

def home(request):
    user = request.user
    #if not user.is_authenticated():
    stores = Store.objects.all()[:10]
    departments = Department.objects.all()
    products = Product.objects.all().order_by('-created_at')
    context = {
            'stores' : stores,
            'departments' : departments,
            'products' : products,
        }
    return render(request, 'main/main.html', context)
    '''
    else:
        return HttpResponseRedirect(reverse('projects:main', args=()))
    '''
    