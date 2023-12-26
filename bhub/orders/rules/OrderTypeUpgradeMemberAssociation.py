from bhub.associates.services import Associate
from bhub.notifications.services import Notification
from bhub.orders.rules.OrderTypeAbsctract import OrderType


class UpgradeMemberAssociation(OrderType, Associate, Notification):
    def execute(self, order):
        self.handle_upgrade_member_association(order)
        self.send_email(order)
        return dict(
            detail=[
                f"Pedido {order.id} - aplicar o upgrade no associado",
                f"Pedido {order.id} - e-mail enviado para proprietário informando sobre a ativação/upgrade",
            ],
            status_code=200,
        )
