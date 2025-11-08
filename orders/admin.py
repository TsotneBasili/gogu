from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'get_total_items', 'total_price', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'user__email', 'shipping_address']
    readonly_fields = ['total_price', 'created_at', 'updated_at']
    list_editable = ['status']
    inlines = [OrderItemInline]

    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'price', 'get_total_price']
    list_filter = ['order__created_at']
    search_fields = ['product__name', 'order__user__username']
    readonly_fields = ['product', 'quantity', 'price']

    def get_total_price(self, obj):
        return f'${obj.get_total_price()}'
    get_total_price.short_description = 'Total Price'
