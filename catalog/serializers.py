from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'is_activated', 'created_at', 'products_count']
        read_only_fields = ['created_at']

    def get_products_count(self, obj):
        return obj.products.count()


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    color_display = serializers.CharField(source='get_color_display', read_only=True)
    material_display = serializers.CharField(source='get_material_display', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'category_name', 'description',
            'price', 'stock', 'is_available', 'featured', 'color', 'color_display',
            'material', 'material_display', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
