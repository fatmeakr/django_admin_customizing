from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

router = DefaultRouter()

router.register("order", OrderViewSet, basename="order")
router.register("product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]
