from unittest import TestCase

from supermarket.SuperMarket import SuperMarket
from supermarket.model.item import BuyItem, Cart


class TestGetTotalCartCost(TestCase):

    def test_it_should_get_total_cast_cost_when_input_cart(self):
        list_item: [BuyItem] = [
            BuyItem(name="coca", total=10, bulk=22),
            BuyItem(name="raudiepca", total=0.5, bulk=1),
        ]
        res = SuperMarket().get_total_prices(list_item=list_item)

        assert res == Cart(total=10.5, items=list_item)
