import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum


class TransactionManager(models.Manager):
    def get_totals(self, user):
        return {
            "income_total": self.filter(user=user, transaction_type="income").aggregate(
                Sum("transaction_amount")
            )["transaction_amount__sum"]
            or 0,
            "expense_total": self.filter(
                user=user, transaction_type="expense"
            ).aggregate(Sum("transaction_amount"))["transaction_amount__sum"]
            or 0,
            "investment_total": self.filter(
                user=user, transaction_type="investment"
            ).aggregate(Sum("transaction_amount"))["transaction_amount__sum"]
            or 0,
        }

    def get_category_details(self, user, category):
        return (
            self.filter(user=user, transaction_type=category)
            .values("transaction_name")
            .annotate(total_amount=models.Sum("transaction_amount"))
        )


class Transaction(models.Model):
    """
    Model representing transactions for a user.
    """

    TRANSACTION_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
        ("investment", "Investment"),
    ]

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_CHOICES, default="Income"
    )
    transaction_name = models.CharField(max_length=150)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    future_transaction_date = models.DateField(
        "Future transaction date", blank=True, null=True
    )

    objects = TransactionManager()

    def __str__(self):
        return f"{self.transaction_name} - {self.transaction_amount}"
