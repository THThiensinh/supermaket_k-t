from unittest import TestCase

from supermarket.SuperMarket import SuperMarket


class TestBuy(TestCase):
    def setUp(self):
        self.store = SuperMarket()

    def test_it_should_buy_with_simple_price(self):
        res = self.store.get_item_price(item_name="coca", bulk=1)

        assert res == {'name': "coca", "total": 0.5}

    def test_it_should_return_bulk_price_when_input_bulk(self):
        res = self.store.get_item_price(item_name="coca", bulk=20)

        assert res == {'name': "coca", "total": 9}

    def test_it_should_return_price_for_bulks_and_retail_price_when_buy_bulk_and_retail(self):
        res = self.store.get_item_price(item_name="coca", bulk=22)

        assert res == {'name': "coca", "total": 10}

    def test_it_should_return_price_for_bulks(self):
        res = self.store.get_item_price(item_name="coca", bulk=40)

        assert res == {'name': "coca", "total": 18}

    def test_it_should_return_price_for_bulks_and_retail(self):
        res = self.store.get_item_price(item_name="coca", bulk=59)

        assert res == {'name': "coca", "total": 27.5}
