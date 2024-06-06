from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'cover_image')
    def cover_image_preview(self, obj):
        if obj.cover_image:
            return mark_safe(f'<img src="{obj.cover_image.url}" width="100" height="150" />')
        return ""

    cover_image_preview.short_description = 'Cover Image'
    cover_image_preview.allow_tags = True
admin.site.register(Book, BookAdmin)