from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image, Place

admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    fields = ('image', 'get_preview', 'position')
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=400,
            height=200,
        )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

