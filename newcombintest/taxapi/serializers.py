from rest_framework import serializers
from .models import Payable, Transaction
from django.db.models import Sum, Count

class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = '__all__'

class UnpaidPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = ('service_description', 'due_date', 'amount_due', 'barcode')

class TransactionSerializer(serializers.ModelSerializer):

    total_count = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = "__all__"

    def get_total_count(self, *args, **kwargs):
        return Transaction.objects.all().count()

    def get_total_amount(self, *args, **kwargs):
        return Transaction.objects.all().aggregate(Sum('amount_paid'))['amount_paid__sum']

