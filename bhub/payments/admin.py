from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin view for Payment"""

    list_display = ["description", "order", "is_paid"]
