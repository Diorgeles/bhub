class Shipping:
    def handle_shipment_for_shipping(self, order):
        return dict(detail=f"Pedido {order.id} - gerar uma guia de remessa para envio")

    def handle_duplicate_shipmentf_for_royalties(self, order):
        return dict(detail=f"Pedido {order.id} - crie uma guia de remessa duplicada para o departamento de royalties")
