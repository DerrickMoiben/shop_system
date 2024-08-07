from django.db import models
from manager.models import Stock
 


class Sales(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
    ]

    stock_item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    sale_price = models.FloatField(editable=False)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    mpesa_code = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the sale price
        self.sale_price = self.quantity_sold * self.stock_item.product_price

        #Ensure that is enough stock available
        if self.stock_item.product_quantity < self.quantity_sold:
            raise ValueError('Not enough stock available')
        # Update the stock
        self.stock_item.product_quantity -= self.quantity_sold
        self.stock_item.save()
        super(Sales, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.stock_item.product_name} - {self.quantity_sold}'