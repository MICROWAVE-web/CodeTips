from django.contrib import admin
from authentication.models import User
from blog.models import Tag, Tip
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = '__all__'

    def clean(self):
        tags = self.cleaned_data.get('tags')
        if tags and tags.count() > 3:
            raise ValidationError('Maximum three tags are allowed.')

        return self.cleaned_data


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    model = User


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Tip)
class PostAdmin(admin.ModelAdmin):
    model = Tip
    form = TipForm

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
