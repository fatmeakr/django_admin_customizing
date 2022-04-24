from rest_framework.serializers import ModelSerializer
from product.models import Product
from order.models import Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id", "user", "status"]

    def create(self, validated_data):
        user = self.context["request"].user
        instance = Order.objects.create(user=user, **validated_data)
        return instance
