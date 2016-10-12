from django.contrib import admin
from items.models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_type', 'parent','name','get_price','get_percent','in_stock','is_new','is_popular']
admin.site.register(Item,ItemAdmin)
