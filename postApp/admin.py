from django.contrib import admin
from postApp.models import *

admin.site.site_title='博客1'
admin.site.site_header='博客2'
admin.site.index_title='博客3'

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','publish_time']
    search_fields = ['content','title']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)