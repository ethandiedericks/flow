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
    list_display = ("user", "income_name", "income_amount", "date_created")
    search_fields = ("income_name",)
    list_filter = ("user",)


@admin.register(IncomeSource)
class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("user",)


@admin.register(ExpenseSource)
class ExpenseSourceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("user",)


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ("user", "investment_name", "investment_amount", "date_created")
    search_fields = ("investment_name",)
    list_filter = ("user",)


@admin.register(InvestmentSource)
class InvestmentSourceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("user",)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "expense_name", "expense_amount", "date_created")
    search_fields = ("expense_name",)
    list_filter = ("user",)
