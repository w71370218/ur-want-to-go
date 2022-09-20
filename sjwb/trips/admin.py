from django.contrib import admin
from .models import Post,  Tag, Comment , Tag_post

class PostAdmin(admin.ModelAdmin):
	list_filter = ('created_date',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Tag_post)

admin.site.site_url = '/'