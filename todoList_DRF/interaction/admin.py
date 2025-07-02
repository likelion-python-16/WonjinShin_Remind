from django.contrib import admin
from .models import Bookmark, Like, Comment, CommentLike


admin.site.register(Like)
admin.site.register(Bookmark)
#admin.site.register(Comment)
admin.site.register(CommentLike)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "todo", "content", "created_at", "like_count")
    
    def like_count(self, obj):
        return obj.likes.count()