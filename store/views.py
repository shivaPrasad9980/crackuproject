from django.shortcuts import render
from .models import Item 
from django.core.paginator import Paginator
# Create your views here.

def items_list(request):
    item_list = Item.objects.all() # To display all items
    sort_by = request.GET.get('sort', 'created_at')
    item_list = item_list.order_by(sort_by)

    paginator = Paginator(item_list, 2)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    return render(request, 'items_list.html', {'items': items})
