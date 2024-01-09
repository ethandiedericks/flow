import re
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
        widgets = {
            "future_transaction_date": forms.DateInput(attrs={"type": "date"}),
            "transaction_amount": forms.NumberInput(
                attrs={"autocomplete": "transaction-amount"}
            ),
            "transaction_type": forms.Select(attrs={"autofocus": True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'error' CSS class to fields with errors

    def clean(self):
        cleaned_data = super().clean()
        transaction_name = cleaned_data.get("transaction_name")
        transaction_amount = cleaned_data.get("transaction_amount")
        if transaction_name is not None and re.search(r"\d", transaction_name):
            self.add_error("transaction_name", "Transaction name can't contain numbers")
        if transaction_amount is not None and transaction_amount <= 0:
            self.add_error(
                "transaction_amount", "Transaction amount must be greater than 0"
            )

        return cleaned_data
