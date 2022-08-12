from django.contrib import admin
from authentication.models import User
from blog.models import Tag, Tip


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    model = User


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Tip)
class PostAdmin(admin.ModelAdmin):
    model = Tip

    list_display = (
        "id",
        "heading",
        "description",
        "date_created",
        "date_modified",
    )
    list_filter = (
        "tags",
        "date_created",
        "date_modified",
    )
    search_fields = (
        "heading",
        "tags",
    )