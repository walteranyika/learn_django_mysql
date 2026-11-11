from django.contrib import admin
from django.contrib.auth.models import User

from app.models import Author, Book

# from app.models import Product


admin.site.site_header ='Admin Portal'
admin.site.site_title='Admin Portal'
admin.site.index_title='System Management'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'names','phone','email')
    search_fields = ('names','phone', 'email')
    ordering = ('names',)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'year','created_at')
    search_fields = ('author', 'title')
    list_filter = ('author', 'year')
    ordering = ('-year',)

#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description','cost', 'price','created_at', 'updated_at')
#     list_display_links = ('id', 'name')
#     list_editable = ('cost', 'price')
#     list_filter = ('created_at',)
#     search_fields = ('name',)
#     ordering = ('-created_at',)

