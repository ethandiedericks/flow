from django import forms
from .models import Transaction, Income, Expense, Investment


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["source", "amount", "future_transaction_date"]


class IncomeForm(TransactionForm):
    class Meta(TransactionForm.Meta):
        model = Income
        # You can add specific fields or customize as required for Income transactions


class ExpenseForm(TransactionForm):
    class Meta(TransactionForm.Meta):
        model = Expense
        # Add specific fields or customize for Expense transactions


class InvestmentForm(TransactionForm):
    class Meta(TransactionForm.Meta):
        model = Investment
        # Add specific fields or customize for Investment transactions
