from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_name",
        "transaction_amount",
        "transaction_type",
        "user",
        "date_created",
    )
    list_filter = ("transaction_type", "user", "date_created")
    search_fields = ("transaction_name", "transaction_type")
    ordering = ("-date_created",)


admin.site.register(Transaction, TransactionAdmin)
