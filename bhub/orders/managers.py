from django.db.models import Manager

from bhub.associates.services import Associate
from bhub.notifications.services import Notification
from bhub.payments.services import PaymentHelpers
from bhub.products.services import Product
from bhub.shipments.services import Shipping


class PostPaymentOrderManager(Manager, Notification, PaymentHelpers, Associate, Shipping, Product):
    def execute(self, order):
        match order.order_type:
            case "physical_product":
                self.handle_shipment_for_shipping(order)
                self.pay_commision(order)
            case "book":
                self.handle_duplicate_shipmentf_for_royalties(order)
            case "member_association":
                self.handle_active_member_association(order)
                self.send_email(order)
            case "upgrade_member_association":
                self.handle_upgrade_member_association(order)
                self.send_email(order)
            case "video":
                self.handle_add_video(order)
