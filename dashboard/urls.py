from django.urls import path
from .views import (
    get_incomes,
    get_expenses,
    get_investments,
    dashboard,
    get_totals,
)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("get_incomes/", get_incomes, name="get_incomes"),
    path("get_expenses/", get_expenses, name="get_expenses"),
    path("get_investments/", get_investments, name="get_investments"),
    path(
        "get_totals/", get_totals, name="get_totals"
    ),  # Make sure the path ends with a trailing slash
]
