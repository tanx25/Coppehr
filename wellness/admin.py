from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Venue, Event, Resource, Announcement, HealthTip


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'url']
    list_filter = ['type']
    search_fields = ['name', 'url']
    ordering = ['type', 'name']


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'expiration_date', 'status', 'published_on',
                    'created_on', 'updated_on', 'category']
    list_filter = ['status', 'release_date', 'expiration_date', 'published_on', 'created_on',
                   'updated_on', 'category']
    search_fields = ['title', 'text']
    date_hierarchy = 'expiration_date'
    ordering = ['status', 'release_date', 'expiration_date']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'status', 'published_on', 'category',
                    'series_title', 'created_on', 'updated_on', 'venue']
    list_filter = ['status', 'category', 'series_title', 'release_date', 'published_on', 'venue']
    search_fields = ['series_title', 'title', 'description']
    date_hierarchy = 'release_date'
    ordering = ['status', 'release_date']
    prepopulated_fields = {
        'slug': ('title', ),
        'art_uri': ('title', )
    }


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'status', 'published_on', 'category',
                    'series_title', 'created_on', 'updated_on', 'venue']
    list_filter = ['status', 'category', 'series_title', 'release_date', 'published_on', 'venue']
    search_fields = ['series_title', 'title', 'description']
    date_hierarchy = 'release_date'
    ordering = ['status', 'release_date']
    prepopulated_fields = {
        'slug': ('title', ),
        'art_uri': ('title', )
    }


@admin.register(HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'expiration_date', 'status', 'published_on',
                    'created_on', 'updated_on']
    list_filter = ['status', 'release_date', 'expiration_date', 'published_on', 'created_on',
                   'updated_on']
    search_fields = ['title', 'text']
    date_hierarchy = 'release_date'
    ordering = ['status', 'release_date']
