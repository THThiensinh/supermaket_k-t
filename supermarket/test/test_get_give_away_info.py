import datetime
from unittest import TestCase

from supermarket.SuperMarket import SuperMarket
from supermarket.model.item import BuyItem


class TestGetGiveAwayInfo(TestCase):
    def test_it_should_return_available_give_away_when_buy_in_specific_time(self):
        item = BuyItem(name="lowCarbMonster", total=600, bulk=20)
        res = SuperMarket().get_give_away_info(item=item, buy_date=datetime.datetime(2022, 10, 25))

        assert res == [{'item': "lowCarbMonster", "total": 3}]

    def test_it_should_return_all_available_give_away_when_buy_time_valid_all_give_time(self):
        item = BuyItem(name="lowCarbMonster", total=600, bulk=20)
        res = SuperMarket().get_give_away_info(item=item, buy_date=datetime.datetime(2022, 9, 3))

        assert res == [
            {"item": "lowCarbMonster",
             "total": 3
             },
            {
                "item": "coca",
                "total": 6
            }
        ]
