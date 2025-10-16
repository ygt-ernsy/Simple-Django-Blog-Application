from django.contrib import admin

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Date informaiton", {"fields": ["created_at","updated_at"], "classes": ["collapse"]}),
        ("Content",{"fields": ["content"], "classes":["collapse"]}),
    ]
    readonly_fields = ("created_at", "updated_at")
    list_display = ["title", "created_at", "updated_at", "was_updated_recently"]
    list_filter = ["updated_at"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
