from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # links to edit page
    list_filter = ('realtor', ) # filter by realtor
    list_editable = ('is_published',) # edit is_published from list view
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') # search by these fields
    list_per_page = 25 # number of listings per page

admin.site.register(Listing, ListingAdmin)


