from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('title', 'views', 'active', 'image_thumbnail', 'created_at', 'updated_at', 'edit_link')

    # Add search capability for title and content
    search_fields = ('title', 'content')

    # Add filters for the sidebar
    list_filter = ('created_at', 'updated_at', 'active', 'views')

    # Method to show a thumbnail of the image
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return 'No Image'
    
    image_thumbnail.short_description = 'Image Preview'

    # Method to create a link to the custom edit page
    def edit_link(self, obj):
        url = reverse('custom_edit_blog_post', args=[obj.pk])
        return format_html('<a href="{}">Edit</a>', url)
    
    edit_link.short_description = 'Edit'
