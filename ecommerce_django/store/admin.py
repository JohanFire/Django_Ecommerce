from django.contrib import admin
from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("product_name", )} # auto fill slug with product name
    list_display= ("product_name", "price", "stock", "category", "is_available","modified_date")

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)