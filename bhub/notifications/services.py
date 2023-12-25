class Notification:
    def send_email(self, order):
        return dict(detail=f"Pedido {order.id} - e-mail enviado para proprietário informando sobre a ativação/upgrade")
