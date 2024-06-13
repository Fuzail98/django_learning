from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/detail.html', context)
