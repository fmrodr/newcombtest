from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PayableSerializer, UnpaidPayableSerializer, TransactionSerializer
from .models import Payable, Transaction, TypeOfService

# Create your views here.
class PayableViewSet(viewsets.ModelViewSet):
    queryset = Payable.objects.all()
    serializer_class = PayableSerializer

    def get_queryset(self):

        queryset = Payable.objects.all()
        
        type = self.request.query_params.get('type')
        if type :
            self.serializer_class = UnpaidPayableSerializer
            service = TypeOfService.objects.get(type_of_service=type)
            queryset = queryset.filter(type_of_service=service)

        not_paid =  self.request.query_params.get('not_paid')
        if not_paid and not_paid == 'true':
            queryset = Payable.objects.exclude(status='paid')
        
        return queryset

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')
        if from_date and to_date:
            queryset = queryset.filter(date__range=[from_date, to_date])
        return queryset

