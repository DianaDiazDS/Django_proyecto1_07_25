from django.contrib import admin

# Register your models here.
from .models import Menus
from .models import MenuCategory
admin.site.register(Menus)
admin.site.register(MenuCategory)