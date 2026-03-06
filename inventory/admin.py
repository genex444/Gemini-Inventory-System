    # admin.py
from django.contrib import admin
from .models import InventoryItem, Category, Status, Room


admin.site.register(InventoryItem)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Status)