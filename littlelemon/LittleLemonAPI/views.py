from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import MenuItem

# Create your views here.
def add_menu_item(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
        data = {'dish': item.name, 'price': item.price}
    except MenuItem.DoesNotExist:
        return JsonResponse({'data':'wrong url'})
    return JsonResponse(data)