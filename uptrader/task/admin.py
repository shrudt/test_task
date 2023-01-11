from django.contrib import admin

from .models import Menu, Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'slug')
    repopulated_fields = {"slug": ("title",)}


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    repopulated_fields = {"slug": ("title",)}


admin.site.register(Item, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
