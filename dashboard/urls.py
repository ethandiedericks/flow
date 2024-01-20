from django.urls import path
from .views import (
    get_incomes,
    get_expenses,
    get_investments,
    dashboard,
    get_totals,
    edit_transaction,
    fetch_edit_transaction_form,
    delete_transaction,
)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("get_incomes/", get_incomes, name="get_incomes"),
    path("get_expenses/", get_expenses, name="get_expenses"),
    path("get_investments/", get_investments, name="get_investments"),
    path("get_totals/", get_totals, name="get_totals"),
    path(
        "edit-transaction/<uuid:transaction_id>/",
        edit_transaction,
        name="edit_transaction",
    ),
    path(
        "edit-transaction/<uuid:transaction_id>/fetch/",
        fetch_edit_transaction_form,
        name="fetch_edit_transaction_form",
    ),
    path(
        "edit-transaction/<uuid:transaction_id>/delete/",
        delete_transaction,
        name="delete_transaction",
    ),
]
