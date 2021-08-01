from django.contrib import admin
from .models import GamePost, AboutUs, ContactUs

@admin.register(GamePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'position', 'social_icon_first', 'social_icon_second', 'person_img')
    list_filter = ('position', 'surname')
    search_fields = ('first_name', 'surname', 'position')

@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_display = ('address_email', 'social_media_first', 'social_media_second')