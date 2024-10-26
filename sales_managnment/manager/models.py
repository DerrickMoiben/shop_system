from django.db import models # type: ignore

# Create your models here.

class Stock(models.Model):
    product_name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name
    
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    employee_salary = models.FloatField()
    employee_phone = models.CharField(max_length=100)
    employee_national_id = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name