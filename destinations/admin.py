from django.contrib import admin
from .models import City, Attraction, Hotel, Restaurant,Package


class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'price', 'duration_days')
    list_display_links = ('name',)
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
    list_per_page = 20





# ---------------------------
# City Admin
# ---------------------------
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')
    list_display_links = ('name',)  # Click name to edit
    search_fields = ('name', 'description')  # Optional: search by name or description
    list_per_page = 20  # Optional: pagination

# ---------------------------
# Attraction Admin
# ---------------------------
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'entry_fee', 'image')
    list_display_links = ('name',)
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
    list_per_page = 20

# ---------------------------
# Hotel Admin
# ---------------------------
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'phone', 'website')
    list_display_links = ('name',)
    search_fields = ('name', 'city__name', 'address')
    list_filter = ('city',)
    list_per_page = 20

# ---------------------------
# Restaurant Admin
# ---------------------------
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'phone', 'website')
    list_display_links = ('name',)
    search_fields = ('name', 'city__name', 'address')
    list_filter = ('city',)
    list_per_page = 20

# ---------------------------
# Register Models
# ---------------------------
admin.site.register(City, CityAdmin)
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Package, PackageAdmin)
