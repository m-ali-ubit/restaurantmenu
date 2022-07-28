from django.contrib import admin

from restaurantmenu.menu.models import Section, Item, Modifier

admin.site.site_header = "Restaurant Menu"

admin.site.register(Section)
admin.site.register(Item)
admin.site.register(Modifier)
