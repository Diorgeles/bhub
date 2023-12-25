from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

from bhub.orders.managers import PostPaymentOrderManager


class Order(TimeStampedModel, SoftDeletableModel):
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    ORDER_TYPE = [
        ("physical_product", "Produto fisico"),
        ("book", "Livro"),
        ("member_association", "Associação de membro"),
        ("upgrade_member_association", "Updgrade de associação de membro"),
        ("video", "Video"),
    ]

    name = models.CharField("Nome do pedido", max_length=50)
    amount = models.DecimalField("Valor", max_digits=9, decimal_places=2)
    order_type = models.CharField("Tipo de pedido", choices=ORDER_TYPE, max_length=100)

    objects_post_payment = PostPaymentOrderManager()
    history = AuditlogHistoryField()

    def __str__(self):
        return self.name


auditlog.register(Order)
