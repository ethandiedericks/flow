from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse


from .models import Transaction
from .forms import TransactionForm


class TransactionView(LoginRequiredMixin, View):
    template_name = "budget/budget.html"

    def get(self, request):
        form = TransactionForm()
        transactions = Transaction.objects.filter(user=request.user).order_by(
            "transaction_type"
        )
        totals = Transaction.objects.get_totals(request.user)
        context = {
            "form": form,
            "transactions": transactions,
            **totals,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()

            # Return JsonResponse for successful form submission
            return JsonResponse(
                {
                    "message": "Transaction created successfully",
                    "transaction": {
                        "transaction_type": transaction.transaction_type,
                        "transaction_name": transaction.transaction_name,
                        "transaction_amount": transaction.transaction_amount,
                        "id": transaction.id,
                    },
                }
            )

        # Return JsonResponse for unsuccessful form submission
        errors = form.errors
        return JsonResponse({"errors": errors}, status=400)


class DeleteTransactionView(LoginRequiredMixin, View):
    def post(self, request, id):
        if request.method == "POST":
            transaction = get_object_or_404(Transaction, pk=id, user=request.user)

            if transaction.user == request.user:
                transaction.delete()
                return JsonResponse({"message": "Transaction deleted successfully"})
            else:
                return JsonResponse(
                    {"message": "Transaction does not belong to the current user"},
                    status=403,
                )
        else:
            return JsonResponse({"message": "Invalid request method"}, status=405)


class GetTotalsView(LoginRequiredMixin, View):
    def get(self, request):
        updated_totals = Transaction.objects.get_totals(request.user)

        return JsonResponse(updated_totals)
