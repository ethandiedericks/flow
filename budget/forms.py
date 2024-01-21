import re

from django import forms
from django.utils.timezone import now
from django.http import JsonResponse

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
            "transaction_type": forms.Select(attrs={"autofocus": True}),
            "transaction_name": forms.TextInput(attrs={"placeholder": "Salary"}),
            "transaction_amount": forms.NumberInput(
                attrs={"autocomplete": "transaction-amount", "placeholder": "24950.50"}
            ),
            "future_transaction_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        # get data
        transaction_name = cleaned_data.get("transaction_name")
        transaction_amount = cleaned_data.get("transaction_amount")
        future_transaction_date = cleaned_data.get("future_transaction_date")

        # check if transaction_name contains digits
        if transaction_name is not None and re.search(r"\d", transaction_name):
            self.add_error("transaction_name", "Transaction name can't contain numbers")
        # check if transaction_amount is less than or equal to zero
        if transaction_amount is not None and transaction_amount <= 0:
            self.add_error(
                "transaction_amount", "Transaction amount must be greater than 0"
            )
        # checks if chosen date is in the future
        if future_transaction_date:
            today = now().date()
            if future_transaction_date <= today:
                self.add_error(
                    "future_transaction_date",
                    "Transaction date should be in the future",
                )

        return cleaned_data

    def as_json(self):
        """
        Convert form errors to a JSON format suitable for Ajax responses.
        """
        errors = {}
        for field, messages in self.errors.items():
            errors[field] = [str(message) for message in messages]
        return JsonResponse({"errors": errors})
