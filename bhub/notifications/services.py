class Notification:
    def send_email(self, order):
        print(f"Pedido {order.id} - e-mail enviado para proprietário informando sobre a ativação/upgrade")
