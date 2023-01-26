from django.contrib import admin
from .models import Event, Food

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img', 'description', 'date')
    list_display_links = ('id', 'title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img', 'description', 'category', 'address', 'menu', 'video', 'rating', 'open', 'close')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title',)
    list_editable = ('rating',)
    list_filter = ('category',)


admin.site.register(Event, EventAdmin)
admin.site.register(Food, FoodAdmin)
