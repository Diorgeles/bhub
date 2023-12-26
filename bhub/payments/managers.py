from django.db.models import Manager

from bhub.orders.models import Order
from bhub.payments.services import PaymentHelpers


class PaymentManager(Manager, PaymentHelpers):
    def pay(self, order):
        print("Pagamento salvo localmente...")
        print("Executa pagamento...")
        return Order.objects_post_payment.execute(order)
