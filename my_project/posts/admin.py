from django.contrib import admin
from .models import Post


# Customizing the PostAdmin with advanced features
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'word_count', 'description_preview')  # Enhanced display
    list_filter = ('title',)  # Filtering options
    search_fields = ('title', 'decription')  # Search functionality
    ordering = ('title',)  # Default ordering
    list_per_page = 20  # Paginate list view
    actions = ['mark_long_descriptions']  # Custom admin actions

    def short_description(self, obj):
        """Return a truncated description for better overview."""
        return obj.decription[:75] + ('...' if len(obj.decription) > 75 else '')

    short_description.short_description = 'Short Description'

    def word_count(self, obj):
        """Calculate and display the word count of the description."""
        return len(obj.decription.split())

    word_count.short_description = 'Word Count'

    def description_preview(self, obj):
        """Generate a detailed preview of the description."""
        if len(obj.decription) > 200:
            return f"{obj.decription[:200]}... (click to read more)"
        return obj.decription

    description_preview.short_description = 'Description Preview'

    def mark_long_descriptions(self, request, queryset):
        """Mark posts with descriptions longer than 1000 characters."""
        long_posts = queryset.filter(decription__length__gt=1000)
        count = long_posts.update(title='LONG POST')
        self.message_user(request, f"{count} posts updated as LONG POST.")

    mark_long_descriptions.short_description = 'Mark posts with long descriptions'

# Registering the Post model with the customized admin
admin.site.register(Post, PostAdmin)