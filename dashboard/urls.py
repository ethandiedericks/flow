from django.urls import path
from .views import get_incomes, get_expenses, get_investments

urlpatterns = [
    path("get_incomes/", get_incomes, name="get_incomes"),
    path("get_expenses/", get_expenses, name="get_expenses"),
    path("get_investments/", get_investments, name="get_investments"),
]
