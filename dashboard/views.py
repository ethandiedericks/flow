from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from budget.models import Transaction
from budget.forms import TransactionForm
from .serializers import GroupedSerializer


@login_required
def dashboard(request):
    is_dashboard_page = request.path.startswith("/dashboard/")
    transactions = Transaction.objects.filter(user=request.user)
    totals = Transaction.objects.get_totals(request.user)
    return render(
        request,
        "dashboard/dashboard.html",
        {
            "is_dashboard_page": is_dashboard_page,
            "transactions": transactions,
            "total_incomes": totals["income_total"],
            "total_expenses": totals["expense_total"],
            "total_investments": totals["investment_total"],
        },
    )


@login_required
def get_grouped_data(request, transaction_type):
    # Fetch real data from your database
    grouped_data = (
        Transaction.objects.filter(user=request.user, transaction_type=transaction_type)
        .values("transaction_name")
        .annotate(total_amount=Sum("transaction_amount"))
    )

    # Serialize the data
    serialized_transactions = GroupedSerializer(grouped_data, many=True)

    labels = [item["transaction_name"] for item in serialized_transactions.data]
    values = [item["total_amount"] for item in serialized_transactions.data]

    return JsonResponse({"labels": labels, "values": values}, safe=False)


@login_required
def get_incomes(request):
    return get_grouped_data(request, "income")


@login_required
def get_expenses(request):
    return get_grouped_data(request, "expense")


@login_required
def get_investments(request):
    return get_grouped_data(request, "investment")


@login_required
def get_totals(request):
    user = request.user
    totals = Transaction.objects.get_totals(user)

    # Retrieve detailed data for each category
    income_details = list(Transaction.objects.get_category_details(user, "income"))
    expense_details = list(Transaction.objects.get_category_details(user, "expense"))
    investment_details = list(
        Transaction.objects.get_category_details(user, "investment")
    )

    response_data = {
        "total_incomes": totals["income_total"],
        "total_expenses": totals["expense_total"],
        "total_investments": totals["investment_total"],
        "income_details": income_details,
        "expense_details": expense_details,
        "investment_details": investment_details,
    }

    return JsonResponse(response_data)


@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = TransactionForm(instance=transaction)

    if request.is_ajax():
        # If the request is an AJAX request, render only the form and return it as JSON
        form_html = render_to_string(
            "dashboard/edit_transaction_form.html",
            {"form": form, "transaction": transaction},
        )
        return JsonResponse({"form_html": form_html})
    else:
        # If it's a regular request, render the full page with the form
        return render(
            request,
            "dashboard/edit_transaction.html",
            {"form": form, "transaction": transaction},
        )


@login_required
def fetch_edit_transaction_form(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    form = TransactionForm(instance=transaction)
    return render(
        request,
        "dashboard/edit_transaction_form.html",
        {"form": form, "transaction": transaction},
    )


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    if request.method == "POST":
        transaction.delete()
        return redirect("dashboard")

    return render(
        request, "dashboard/delete_transaction.html", {"transaction": transaction}
    )
