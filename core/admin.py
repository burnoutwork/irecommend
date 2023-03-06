from django.contrib import admin

from .models import City, Category, Product, Review

admin.site.site_header = 'Irecommend admin'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')
    search_fields = ('title', 'creator')
    list_filter = ('category', 'city')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'creator')
    search_fields = ('title', 'product', 'creator')
