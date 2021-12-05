from django.db import models

# Create your models here.
class Payable(models.Model):
    type_of_service = models.ForeignKey('TypeOfService', on_delete=models.CASCADE)
    service_description = models.CharField(max_length=255)
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.service_description

class TypeOfService(models.Model):
    type_of_service = models.CharField(max_length=255)

    def __str__(self):
        return self.type_of_service

class Transaction(models.Model):
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    card_number = models.CharField(max_length=255)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.card_number

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return self.payment_method
