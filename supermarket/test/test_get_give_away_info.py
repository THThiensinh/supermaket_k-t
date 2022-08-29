import datetime
from unittest import TestCase

from supermarket.SuperMarket import SuperMarket
from supermarket.model.item import BuyItem


class TestGetGiveAwayInfo(TestCase):
    def test_it_should_return_available_give_away_when_buy_in_specific_time(self):
        item = BuyItem(name="lowCarbMonster", total=600, bulk=20)
        res = SuperMarket().get_give_away_info(item=item, buy_date=datetime.datetime(2022, 10, 25))

        assert res == [{'item': "lowCarbMonster", "total": 3, "product": item.name}]

    def test_it_should_return_all_available_give_away_when_buy_time_valid_all_give_time(self):
        item = BuyItem(name="lowCarbMonster", total=600, bulk=20)
        res = SuperMarket().get_give_away_info(item=item, buy_date=datetime.datetime(2022, 9, 3))

        assert res == [
            {
                "item": "lowCarbMonster",
                "total": 3,
                "product": item.name
             },
            {
                "item": "coca",
                "total": 6,
                "product": item.name
            }
        ]

    def test_it_should_return_none_when_all_give_away_are_pass(self):
        item = BuyItem(name="lowCarbMonster", total=600, bulk=20)
        res = SuperMarket().get_give_away_info(item=item, buy_date=datetime.datetime(2022, 11,11))

        assert res == []

    def test_it_should_return_none_when_item_not_have_any_give_away(self):
        item = BuyItem(name="thit_heo", total=600, bulk=20)
        res = SuperMarket().get_give_away_info(item=item, buy_date=datetime.datetime(2022, 11,11))

        assert res == []