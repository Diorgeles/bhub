from django.db.models import Manager

from bhub.orders.rules import (
    Book,
    MemberAssociation,
    PhysicalProduct,
    UpgradeMemberAssociation,
    Video,
)


class PostPaymentOrderManager(Manager):
    def execute(self, order):
        match order.order_type:
            case "physical_product":
                return PhysicalProduct().execute(order)
            case "book":
                return Book().execute(order)
            case "member_association":
                return MemberAssociation().execute(order)
            case "upgrade_member_association":
                return UpgradeMemberAssociation().execute(order)
            case "video":
                return Video().execute(order)
