from django.contrib import admin
from .models import Postpage


@admin.register(Postpage)
class PostpageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "district", "price", "status", "created_at", "views")
    list_filter = ("category", "status", "district")
    search_fields = ("title", "seller", "district", "description")
