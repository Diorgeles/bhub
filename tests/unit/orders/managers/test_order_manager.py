from pytest import mark

from bhub.orders.models import Order
from bhub.payments.models import Payment


@mark.only
class TestUnitOrderManager:
    @mark.django_db
    def test_pay_order(self):
        order = Order.objects.create(name="Teste1", amount=10, order_type="physical_product")
        Payment.objects.pay(order)
        print(order.order_type)
