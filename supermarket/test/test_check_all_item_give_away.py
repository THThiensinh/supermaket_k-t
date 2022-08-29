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

        assert res == [
            {'item': 'raudiepca', 'total': 7, "product": "coca"},
            {'item': 'lowCarbMonster', 'total': 3, "product": "lowCarbMonster"},
            {'item': 'coca', 'total': 6, "product": "lowCarbMonster"}
        ]

    def test_it_should_return_empty_list_when_list_item_input_is_empty(self):
        list_item = []

        res = SuperMarket().get_all_give_away_for_item_in_cart(
            list_item=list_item,
            buy_date=datetime.datetime(2022, 9, 3)
        )

        assert res == []

    def test_it_should_return_empty_list_when_list_item_not_have_any_give_away(self):
        list_item: [BuyItem] = [
            BuyItem(name="raudiepca", total=0.5, bulk=1),
        ]
        res = SuperMarket().get_all_give_away_for_item_in_cart(
            list_item=list_item,
            buy_date=datetime.datetime(2022, 9, 3)
        )

        assert res == []
