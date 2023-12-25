from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

from bhub.orders.models import Order
from bhub.payments.managers import PaymentManager


class Payment(TimeStampedModel, SoftDeletableModel):
    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    description = models.CharField("Descrição do pagamento", max_length=50)
    order = models.ForeignKey(Order, related_name="payment_order", on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField("Pago", default=False)

    objects = PaymentManager()
    history = AuditlogHistoryField()

    def __str__(self):
        return self.description


auditlog.register(Payment)
