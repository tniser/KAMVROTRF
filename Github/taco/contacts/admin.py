from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'contacts_date', 'contacts_name', 'contacts_email', 'contacts_called')
    list_display_links = ('contacts_date', 'contacts_name', 'contacts_email')
    list_filter = ('contacts_date', 'contacts_called')
    list_editable = ('contacts_called',)
    search_fields = ('contacts_date', 'contacts_name', 'contacts_email')

admin.site.register(Contact, ContactAdmin)

admin.site.register(MenuCategory)

class MenuNameAdmin(admin.ModelAdmin):
    list_display = ('menu_category', 'menu_name')
    list_display_links = ('menu_name',)
    list_editable = ('menu_category',)

admin.site.register(MenuName, MenuNameAdmin)

class MenuPriceAdmin(admin.ModelAdmin):
    list_display = ('price_name', 'price_quant', 'price_price')
    list_display_links = ('price_quant', 'price_price')
    list_editable = ('price_name',)

admin.site.register(MenuPrice, MenuPriceAdmin)