from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "transaction_type",
            "transaction_name",
            "transaction_amount",
            "future_transaction_date",
        ]
