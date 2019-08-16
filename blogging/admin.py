from django.contrib import admin
from blogging.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'modified_date',
                    'published_date')
    list_filter = ('created_date', 'category')


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )
    list_display = ('name', 'description')


admin.site.site_header = 'Django Blog Admin Dashboard'

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
