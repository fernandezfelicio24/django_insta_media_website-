from django.contrib import admin


# Register your models here.
from .models import Post, UserProfile, Comment, Notification

class PostAdmin(admin.ModelAdmin):

    readonly_fields = ['slug']

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)