from django.contrib import admin

from .models import Post
# OVERRIDER lại class ModelAdmin
class PostAdmin(admin.ModelAdmin): # thừa kế admin.ModelAdmin
    list_display = ['title','body','date']
    list_filter = ['date']
    search_fields = ['title', 'body']
admin.site.register(Post, PostAdmin)
