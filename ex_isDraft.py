from django.contrib import admin
from testapp.models import Post
     
def make_published(modeladmin, request, queryset):
    """ Make all posts published. """
     queryset.update(is_draft=False)
     make_published.short_description = "Mark selected posts as published"
     
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_draft')
    actions = [make_published]
   
admin.site.register(Post, PostAdmin)
