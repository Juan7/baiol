from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from stores.models import Store, StoreProduct
from products.models import Product, Category, Department, ProductInstance

def home(request):
    user = request.user
    #if not user.is_authenticated():
    stores = Store.objects.all()[:10]
    departments = Department.objects.all()
    products = ProductInstance.objects.all().order_by('-created_at')
    context = {
            'stores' : stores,
            'departments' : departments,
            'products' : products,
        }
    return render(request, 'main/main.html', context)

def store(request, store_id):
    user = request.user
    store = get_object_or_404(Store, id=store_id)
    
    products = StoreProduct.objects.filter(store=store).order_by('-created_at')
    categories = []
    for product in products:
        category = product.product.product.category.all()
        categories += category
        
    #categories = StoreProduct.objects.filter(store=store).order_by('-created_at')
    
    context = {
            'store' : store,
            'categories' : categories,
            'products' : products,
        }
    return render(request, 'main/store.html', context)
    
    