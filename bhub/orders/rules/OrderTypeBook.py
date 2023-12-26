from bhub.orders.rules.OrderTypeAbsctract import OrderType
from bhub.payments.services import PaymentHelpers
from bhub.shipments.services import Shipping


class Book(OrderType, Shipping, PaymentHelpers):
    def execute(self, order):
        self.handle_duplicate_shipmentf_for_royalties(order)
        self.pay_commision(order)
        return dict(
            detail=[
                f"Pedido {order.id} - crie uma guia de remessa duplicada para o departamento de royalties",
                f"Pedido {order.id} - gerar um pagamento de comissão ao agente",
            ],
            status_code=200,
        )
