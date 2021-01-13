from django.contrib import admin

from .models import Post

admin.site.site_header = "HMStein"
admin.site.site_title = "HMStein Admin Area"
admin.site.index_title = "HMStein Admin"

admin.site.register(Post)
