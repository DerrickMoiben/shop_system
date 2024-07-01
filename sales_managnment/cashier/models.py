from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()

    def __str__(self):
        return self.product_name
    
class Sale(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity} - {self.total_price} - {self.payment_method} - {self.date}"