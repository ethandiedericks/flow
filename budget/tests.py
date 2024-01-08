from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Transaction


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = get_user_model().objects.create_user(
            email="testuser@email.com", password="testpassword"
        )

        # Create a transaction for testing
        cls.transaction = Transaction.objects.create(
            user=cls.user,
            transaction_type="Income",
            transaction_name="Test Income",
            transaction_amount=100,
            future_transaction_date="2024-01-08",
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.transaction_type, "Income")
        self.assertEqual(self.transaction.transaction_name, "Test Income")
        self.assertEqual(self.transaction.transaction_amount, 100)
        self.assertEqual(str(self.transaction), "Test Income - 100")

    def test_transaction_date_defaults(self):
        self.assertIsNotNone(self.transaction.date_created)
        self.assertIsNotNone(self.transaction.date_modified)

    def test_future_transaction_date(self):
        self.assertIsNotNone(self.transaction.future_transaction_date)

    def test_transaction_amount_decimal_places(self):
        decimal_places = self.transaction._meta.get_field(
            "transaction_amount"
        ).decimal_places
        self.assertEqual(decimal_places, 2)

    def test_transaction_choices(self):
        choices = dict(self.transaction.TRANSACTION_CHOICES)
        self.assertIn(self.transaction.transaction_type, choices.values())

    def test_transaction_user_relationship(self):
        self.assertEqual(self.transaction.user.email, "testuser@email.com")
