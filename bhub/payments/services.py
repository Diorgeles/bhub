class PaymentHelpers:
    def pay_commision(self, order):
        return dict(detail=f"Pedido {order.id} - gere um pagamento de comissão ao agente")
