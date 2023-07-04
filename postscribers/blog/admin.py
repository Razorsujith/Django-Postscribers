from django.contrib import admin
from .models import PostModel, Comment


admin.site.site_header = 'Razor Blog Admin'

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')


    
admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)
