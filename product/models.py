from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="نام", max_length=100)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class ProductBrnd(models.Model):
    name = models.CharField(verbose_name="نام", max_length=100)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class ProductPrice(models.Model):
    class UnitType(models.IntegerChoices):
        Toman = 0, "Toman"
        Dollar = 1, "Dollar"
        Uro = 2, "Uro"

    price = models.PositiveIntegerField(verbose_name="مقدار عددی قیمت هر کالا")
    unit = models.IntegerField(choices=UnitType.choices)

    def __str__(self):
        return f"{self.price} - {self.unit}"

    def __repr__(self):
        return self.__str__()


class Product(models.Model):
    class Colors(models.IntegerChoices):
        Blue = 0, "Blue"
        Green = 1, "Green"
        Gold = 2, "Gold"

    name = models.CharField(verbose_name="نام", max_length=100)
    color = models.IntegerField(choices=Colors.choices)
    prices = models.ManyToManyField(to=ProductPrice, related_name="prices_products", blank=True)
    brand = models.ForeignKey(
        to=ProductBrnd, on_delete=models.CASCADE, related_name="brnad_products"
    )
    category = models.ForeignKey(
        to=ProductCategory, on_delete=models.CASCADE, related_name="category_products"
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()
