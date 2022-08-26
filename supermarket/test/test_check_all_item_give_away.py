import datetime
from unittest import TestCase

from supermarket.SuperMarket import SuperMarket
from supermarket.model.item import BuyItem


class TestCheckAllItemGiveAway(TestCase):
    def test_it_should_return_all_available_give_away_for_item_when_list_item_valid(self):
        list_item: [BuyItem] = [
            BuyItem(name="coca", total=10, bulk=22),
            BuyItem(name="raudiepca", total=0.5, bulk=1),
            BuyItem(name="lowCarbMonster", total=600, bulk=20)
        ]
        res = SuperMarket().get_all_give_away_for_item_in_cart(
            list_item=list_item,
            buy_date=datetime.datetime(2022, 9, 3)
        )

        assert res == [{'item': "lowCarbMonster", "total": 3}]
