from django.shortcuts import render
from .models import Products
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.urls import reverse_lazy


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)


def detailview(request,pk):
    product_obj = Products.objects.filter(id=pk)[0]

    if cache.get(pk):
        wprod=cache.get(pk)
        print("DATA COMING FROM CACHE")
    else:
        try:
            wprod=Products.objects.all()
            c = cache.set(pk, wprod)
            print("DATA COMING FROM DB")
        except Products.DoesNotExist:
            return redirect('/')

    context={'object':product_obj}
    return render(request,'products/product_detail_view.html',context)

def addtowishlist(request,pk):
    product_obj = Products.objects.filter(id=pk)[0]
    wishlist_obj=Wishlist.objects.get_or_create(
        wishlist_user=request.user,
        wishlist_product=product_obj
    )
    return redirect('dashboard:home')

class Wishlistcbv(ListView):
    model = Wishlist
    template_name = 'products/product_wishlist.html'
    context_object_name = 'products'

    def get_queryset(self):
        query_set=Wishlist.objects.filter(wishlist_user=self.request.user)
        print("query_set", query_set)
        return query_set

class Deletewishlistcbv(DeleteView):
    model = Wishlist
    success_url = reverse_lazy('products:wishlist')
    template_name = 'products/wishlist_confirm_delete.html'

