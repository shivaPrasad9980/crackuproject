from django.contrib import admin
from .models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','created_at']

admin.site.register(Item,ItemAdmin)