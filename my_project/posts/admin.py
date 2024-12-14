from django.contrib import admin
from .models import Post, New, Comment

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


# Customizing the Comment model admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'likes', 'text_snippet')  # Display relevant fields in the list view
    search_fields = ('user__username', 'text')  # Allow search by user and text content
    list_filter = ('created_at', 'likes')  # Filter by creation date and likes
    ordering = ('-created_at',)  # Sort by the newest comments first
    readonly_fields = ('created_at',)  # Make the created_at field read-only

    def text_snippet(self, obj):
        return obj.text[:50]  # Show a snippet of the comment text (first 50 characters)
    text_snippet.short_description = 'Comment Snippet'  # Set custom label for the snippet column


# Customizing the New model admin
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')  # Display relevant fields in the list view
    search_fields = ('title', 'content', 'author')  # Allow search by title, content, and author
    list_filter = ('created_at', 'is_published')  # Filter by creation date and publication status
    ordering = ('-created_at',)  # Sort by the newest news first
    list_editable = ('is_published',)  # Allow inline editing of the publication status in the list view

# Register the models with their customized admin classes
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(New, NewAdmin)
