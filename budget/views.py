from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.views import View

from .models import Transaction
from .forms import TransactionForm


class TransactionView(View):
    template_name = "budget/budget.html"

    def get(self, request):
        form = TransactionForm()
        transactions = Transaction.objects.filter(user=request.user).order_by(
            "transaction_type"
        )
        income_total = (
            transactions.filter(transaction_type="income").aggregate(
                Sum("transaction_amount")
            )["transaction_amount__sum"]
            or 0
        )

        expense_total = (
            transactions.filter(transaction_type="expense").aggregate(
                Sum("transaction_amount")
            )["transaction_amount__sum"]
            or 0
        )

        investment_total = (
            transactions.filter(transaction_type="investment").aggregate(
                Sum("transaction_amount")
            )["transaction_amount__sum"]
            or 0
        )
        context = {
            "form": form,
            "transactions": transactions,
            "income_total": income_total,
            "expense_total": expense_total,
            "investment_total": investment_total,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("budget")
        else:
            transactions = Transaction.objects.filter(user=request.user)

            context = {
                "form": form,
                "transactions": transactions,
            }
            return render(request, self.template_name, context)


class DeleteTransactionView(View):
    def post(self, request, id):
        transaction = get_object_or_404(Transaction, pk=id, user=request.user)

        if transaction.user == request.user:
            transaction.delete()
        return redirect("budget")
