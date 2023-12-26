from bhub.orders.rules.OrderTypeAbsctract import OrderType
from bhub.products.services import Product


class Video(OrderType, Product):
    def execute(self, order):
        self.handle_add_video(order)
        return dict(
            detail=f"Pedido {order.id} - adicione um vídeo gratuito de “Primeiros Socorros” à guia de remessa",
            status_code=200,
        )
