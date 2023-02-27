from django.contrib import admin
from .models import Event, Food, FoodGalery
from .forms import ShowFoodForm


class ShowPhotoInline(admin.TabularInline):
    model = FoodGalery

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
    form = ShowFoodForm
    inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


admin.site.register(Event, EventAdmin)
admin.site.register(Food, FoodAdmin)