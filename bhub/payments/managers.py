from django.db.models import Manager

from bhub.orders.models import Order
from bhub.payments.services import PaymentHelpers


class PaymentManager(Manager, PaymentHelpers):
    def pay(self, order):
        print("Pagamento salvo localmente...")
        print("Executa pagamento...")
        Order.objects_post_payment.execute(order)
        return dict(detail=f"Pedido {order.id} pago com sucesso", status=200)
