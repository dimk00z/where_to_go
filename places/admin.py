from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from .models import Place, Image

# Register your models here.


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ['image',  'place', 'get_preview_image', ]
    raw_id_fields = ['place', ]
    readonly_fields = ['get_preview_image', ]


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['image',  'get_preview_image', ]
    readonly_fields = ['get_preview_image', ]
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title', ]

    # def headshot_image(self, obj):
    #     return format_html('<img src="{url}" height="200"/>'.format(
    #         url=self.image.url,
    #     )
    #     )
    # headshot_image.short_description = 'Предизображение'
