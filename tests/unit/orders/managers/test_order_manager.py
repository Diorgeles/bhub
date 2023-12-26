from pytest import mark

from bhub.orders.models import Order
from bhub.payments.models import Payment


@mark.only
class TestUnitOrderManager:
    @mark.django_db
    def test_pay_order_type_physical_product(self):
        order = Order.objects.create(name="Teste1", amount=10, order_type="physical_product")
        pay = Payment.objects.pay(order)
        assert order is not None
        assert pay is not None

    @mark.django_db
    def test_pay_order_type_book(self):
        order = Order.objects.create(name="Teste1", amount=10, order_type="book")
        pay = Payment.objects.pay(order)
        assert order is not None
        assert pay is not None

    @mark.django_db
    def test_pay_order_type_member_association(self):
        order = Order.objects.create(name="Teste1", amount=10, order_type="member_association")
        pay = Payment.objects.pay(order)
        assert order is not None
        assert pay is not None

    @mark.django_db
    def test_pay_order_type_upgrade_member_association(self):
        order = Order.objects.create(name="Teste1", amount=10, order_type="upgrade_member_association")
        pay = Payment.objects.pay(order)
        assert order is not None
        assert pay is not None

    @mark.django_db
    def test_pay_order_type_video(self):
        order = Order.objects.create(name="Teste1", amount=10, order_type="video")
        pay = Payment.objects.pay(order)
        assert order is not None
        assert pay is not None
