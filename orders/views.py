from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart


@login_required
def order_list_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def create_order_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty. Add items before creating an order.')
        return redirect('cart_view')
    
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address', '')
        notes = request.POST.get('notes', '')
        
        if not shipping_address:
            messages.error(request, 'Shipping address is required.')
            return render(request, 'orders/create_order.html', {'cart': cart})
        
        total_price = cart.get_total_price()
        
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            shipping_address=shipping_address,
            notes=notes,
            status='pending'
        )
        
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
        
        cart.items.all().delete()
        
        messages.success(request, f'Order #{order.id} created successfully!')
        return redirect('order_detail', order_id=order.id)
    
    return render(request, 'orders/create_order.html', {'cart': cart})
