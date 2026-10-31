from django.contrib import admin
from .models import Announcement, PostPage

# Register your models here.
admin.site.register(Announcement)


@admin.register(PostPage)
class PostPageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "district", "price", "status", "created_at", "views")
    list_filter = ("category", "status", "district")
    search_fields = ("id", "title", "seller", "district", "description")