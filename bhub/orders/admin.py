from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin view for Order"""

    list_display = ["name", "amount", "order_type"]
