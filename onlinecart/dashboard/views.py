from django.shortcuts import render
from products.models import Products
from django.views.generic import ListView


def home(request):
    product_obj=Products.objects.all()
    context={'products':product_obj}
    return render(request,'dashboard/home.html',context)


# class based view

# class HomepageViewCBV(ListView):
#     model = Products
#     template_name = 'dashboard/home.html'