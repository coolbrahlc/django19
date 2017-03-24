from django.contrib import admin
from .models import *
# Register your models here.


class ProductImgInline(admin.TabularInline):
    model = ProductImg
    exctra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Product._meta.fields]
    inlines = [ProductImgInline]

    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)


class ProductImgAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in ProductImg._meta.fields]

    class Meta:
        model = ProductImg
admin.site.register(ProductImg, ProductImgAdmin)
