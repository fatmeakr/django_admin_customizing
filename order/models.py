from django.db import models


class Order(models.Model):
    class OrderStatusType(models.IntegerChoices):
        Pending = 0, "Pending"
        Paied = 1, "Paied"
        Failed = 2, "Failed"

    status = models.PositiveSmallIntegerField(choices=OrderStatusType.choices, default=0, null=True)
    user = models.ForeignKey(
        to="user.User", on_delete=models.DO_NOTHING, related_name="user_orders"
    )
    product = models.OneToOneField(
        to="product.Product", on_delete=models.DO_NOTHING, related_name="order"
    )

    def __str__(self):
        return f"{self.user}"

    def __repr__(self):
        return self.__str__()
