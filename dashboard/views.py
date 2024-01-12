from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from budget.models import Transaction
from .serializers import GroupedSerializer


@login_required
def dashboard(request):
    is_dashboard_page = request.path.startswith("/dashboard/")
    return render(
        request, "dashboard/dashboard.html", {"is_dashboard_page": is_dashboard_page}
    )


@login_required
def get_grouped_data(request, transaction_type):
    grouped_data = (
        Transaction.objects.filter(user=request.user, transaction_type=transaction_type)
        .values("transaction_name")
        .annotate(total_amount=Sum("transaction_amount"))
    )

    serialized_transactions = GroupedSerializer(grouped_data, many=True)

    return JsonResponse(serialized_transactions.data, safe=False)


@login_required
def get_incomes(request):
    return get_grouped_data(request, "income")


@login_required
def get_expenses(request):
    return get_grouped_data(request, "expense")


@login_required
def get_investments(request):
    return get_grouped_data(request, "investment")
