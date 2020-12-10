from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from App_Video.models import Category,Video, Comment, Likes


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# Register your models here.

# admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Video,MyModelAdmin)