from django.contrib import admin
from .models import (
    Income,
    Expense,
    Investment,
    IncomeSource,
    ExpenseSource,
    InvestmentSource,
)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "source", "amount", "date_created")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "source", "amount", "date_created")


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "source", "amount", "date_created")


@admin.register(IncomeSource)
class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name")


@admin.register(ExpenseSource)
class ExpenseSourceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name")


@admin.register(InvestmentSource)
class InvestmentSourceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name")
