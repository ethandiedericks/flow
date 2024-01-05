from django.db import models
from django.contrib.auth import get_user_model
import uuid


class TransactionSource(models.Model):
    """
    Base model representing transaction sources for a user.
    """

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class IncomeSource(TransactionSource):
    """
    Model representing sources of income.
    """


class ExpenseSource(TransactionSource):
    """
    Model representing sources of expenses.
    """


class InvestmentSource(TransactionSource):
    """
    Model representing sources of investments.
    """


class Transaction(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    future_transaction_date = models.DateField(blank=True, null=True)
    source = models.ForeignKey(
        TransactionSource, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.source} - {self.amount}"


class Income(Transaction):
    source = models.ForeignKey(
        IncomeSource, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"


class Expense(Transaction):
    source = models.ForeignKey(
        ExpenseSource, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"


class Investment(Transaction):
    source = models.ForeignKey(
        InvestmentSource, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Investment"
        verbose_name_plural = "Investments"
