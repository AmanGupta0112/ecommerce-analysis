from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity_sold = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    review_count = models.IntegerField()

    class Meta:
        db_table = "products"
