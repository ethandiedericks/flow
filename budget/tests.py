from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import (
    Income,
    Expense,
    Investment,
    IncomeSource,
    ExpenseSource,
    InvestmentSource,
)

User = get_user_model()


class TestModels(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            email="testuser@email.com", password="testpassword"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    @classmethod
    def create_income_source(cls):
        return IncomeSource.objects.create(user=cls.user, name="Salary")

    @classmethod
    def create_expense_source(cls):
        return ExpenseSource.objects.create(user=cls.user, name="Rent")

    @classmethod
    def create_investment_source(cls):
        return InvestmentSource.objects.create(user=cls.user, name="Stocks")

    def test_income_creation(self):
        income_source = self.create_income_source()
        income = Income.objects.create(
            user=self.user, amount=1000, source=income_source
        )

        self.assertEqual(income.amount, 1000)
        self.assertEqual(income.user, self.user)
        self.assertEqual(income.source, income_source)

    def test_expense_creation(self):
        expense_source = self.create_expense_source()
        expense = Expense.objects.create(
            user=self.user, amount=500, source=expense_source
        )

        self.assertEqual(expense.amount, 500)
        self.assertEqual(expense.user, self.user)
        self.assertEqual(expense.source, expense_source)

    def test_investment_creation(self):
        investment_source = self.create_investment_source()
        investment = Investment.objects.create(
            user=self.user, amount=2000, source=investment_source
        )

        self.assertEqual(investment.amount, 2000)
        self.assertEqual(investment.user, self.user)
        self.assertEqual(investment.source, investment_source)
