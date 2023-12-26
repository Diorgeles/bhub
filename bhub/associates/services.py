class Associate:
    def handle_active_member_association(self, order):
        print(f"Pedido {order.id} - ativar associação")

    def handle_upgrade_member_association(self, order):
        print(f"Pedido {order.id} - aplicar o upgrade de associação")
