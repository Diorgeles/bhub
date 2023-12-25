from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

from bhub.orders.models import Order


class Payment(TimeStampedModel, SoftDeletableModel):
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    description = models.CharField("Descrição do pagamento", max_length=50)
    amount = models.DecimalField("Valor", max_digits=9, decimal_places=2)
    order = models.ForeignKey(Order, related_name="payment_order", on_delete=models.SET_NULL, null=True, blank=True)

    history = AuditlogHistoryField()

    def __str__(self):
        return self.description


auditlog.register(Payment)
