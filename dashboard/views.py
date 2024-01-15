from django.db.models import Sum

from budget.models import Transaction
from .serializers import GroupedSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    is_dashboard_page = request.path.startswith("/dashboard/")
    transactions = Transaction.objects.filter(user=request.user)

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "is_dashboard_page": is_dashboard_page,
            "transactions": transactions,
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
