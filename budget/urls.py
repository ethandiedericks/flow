from django.urls import path
from . import views

urlpatterns = [
    path("", views.TransactionView.as_view(), name="budget"),
    path(
        "delete_transaction/<uuid:id>/",
        views.DeleteTransactionView.as_view(),
        name="delete_transaction",
    ),
]
