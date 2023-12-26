class Notification:
    def send_email(self, order):
        print("Colocando email na fila de processamento...")
        print(f"Pedido {order.id} - e-mail enviado para proprietário informando sobre a ativação/upgrade")
