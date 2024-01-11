# budget/urls.py
from django.urls import path
from .views import TransactionView, DeleteTransactionView, GetTotalsView

urlpatterns = [
    path("", TransactionView.as_view(), name="budget"),
    path(
        "delete_transaction/<uuid:id>/",
        DeleteTransactionView.as_view(),
        name="delete_transaction",
    ),
    path("get_totals/", GetTotalsView.as_view(), name="get_totals"),
]
