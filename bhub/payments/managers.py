from django.db.models import Manager

from bhub.orders.models import Order
from bhub.payments.services import PaymentHelpers


class PaymentManager(Manager, PaymentHelpers):
    def pay(self, order):
        print("Pagamento salvo localmente...")
        print("Executa pagamento...")
        self.create(description=f"Pagamento de {order.name}", order=order, is_paid=True)
        return Order.objects_post_payment.execute(order)
