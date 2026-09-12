from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    # قم بإلغاء أو تعديل prepopulated_fields و list_filter إذا لم تكن هذه الحقول (slug/updated) موجودة في models.py