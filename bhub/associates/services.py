class Associate:
    def handle_active_member_association(self, order):
        return dict(detail=f"Pedido {order.id} - ativar associação")

    def handle_upgrade_member_association(self, order):
        return dict(detail=f"Pedido {order.id} - aplique o upgrade")
