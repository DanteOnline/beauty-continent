from django.contrib import admin
from categories.models import Category, Subcategory

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('order','name')
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('order','name','parent','is_get_image')

    #Для удаления без pre_delete
    '''actions = ['really_delete_selected']

    def get_actions(self, request):
        actions = super(SubcategoryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 запись была удалена"
        else:
            message_bit = "%s записи были удалены" % queryset.count()
        self.message_user(request, message_bit)

    really_delete_selected.short_description = "Удалить выбранные записи"'''

admin.site.register(Subcategory,SubcategoryAdmin)