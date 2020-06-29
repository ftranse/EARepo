from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'comment', 'created_at', 'updated_at', 'is_published', 'get_diagram')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'comment')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'comment', 'diagram', 'get_diagram', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_diagram', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_diagram(self, obj):
        if obj.diagram:
            return mark_safe(f'<img src="{ obj.diagram.url }" width="75">')
        else:
            return '-'

    get_diagram.short_description = 'Диаграмма'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление приложениями'
admin.site.site_header = 'Управление приложениями'
