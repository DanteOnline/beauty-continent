from django.contrib import admin
from goods.models import Good, GoodImage
from django_comments.models import Comment

# Register your models here.
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name','category','price', 'is_with_discount', 'in_stock', 'is_new', 'is_popular']
admin.site.register(Good, GoodAdmin)

class GoodImageAdmin(admin.ModelAdmin):
    list_display = ['good']
admin.site.register(GoodImage, GoodImageAdmin)

class MyCommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'submit_date', 'is_public', 'is_removed')

admin.site.unregister(Comment)
admin.site.register(Comment, MyCommentsAdmin)