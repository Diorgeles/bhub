from bhub.orders.rules.OrderTypeAbsctract import OrderType
from bhub.payments.services import PaymentHelpers
from bhub.shipments.services import Shipping


class PhysicalProduct(OrderType, Shipping, PaymentHelpers):
    def execute(self, order):
        self.handle_shipment_for_shipping(order)
        self.pay_commision(order)
        return dict(
            detail=[
                f"Pedido {order.id} - gerar uma guia de remessa para envio",
                f"Pedido {order.id} - gerar um pagamento de comissão ao agente",
            ],
            status_code=200,
        )
