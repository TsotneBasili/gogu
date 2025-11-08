from rest_framework.routers import DefaultRouter
from catalog.api_views import CategoryViewSet, ProductViewSet
from cart.api_views import CartViewSet
from orders.api_views import OrderViewSet
from accounts.api_views import UserViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
