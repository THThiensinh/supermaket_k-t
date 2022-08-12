import datetime

from pydash import py_, sum_, in_range

from supermarket.model.item import BuyItem, Cart


class SuperMarket:
    products = [
        {"name": "coca", "price": 0.5, "bulk": 20, "bulk_price": 9},
        {"name": "raudiepca", "price": 0.5, "bulk": 20, "bulk_price": 9},
        {"name": "lowCarbMonster", "price": 30, "bulk": 1, "bulk_price": 30},
    ]

    give_away_product = [
        {"product": "lowCarbMonster", "buy": 3, "give_away": "lowCarbMonster", "deal": 1,
         "day_start": datetime.datetime(2020, 6, 1), "day_end": datetime.datetime(2020, 10, 28), "status": "end"},
        {"product": "lowCarbMonster", "buy": 6, "give_away": "lowCarbMonster", "deal": 1,
         "day_start": datetime.datetime(2022, 6, 1), "day_end": datetime.datetime(2022, 10, 28), "status": "ongoing"},
        {"product": "lowCarbMonster", "buy": 3, "give_away": "coca", "deal": 1,
         "day_start": datetime.datetime(2022, 6, 1), "day_end": datetime.datetime(2022, 9, 6), "status": "ongoing"}
    ]

    def get_item_price(self, item_name: str, bulk: int):
        sale_item = py_.find(self.products, lambda item: item.get('name') == item_name)

        if bulk == sale_item.get("bulk"):
            total = sale_item.get("bulk_price")
            return BuyItem(name=item_name, total=total, bulk=bulk)

        if bulk > sale_item.get("bulk"):
            item_bulk = sale_item.get("bulk")
            price = sale_item.get("bulk_price")
            item_price = sale_item.get("price")

            bulk_price = bulk // item_bulk * price
            retail_price = bulk % item_bulk * item_price
            total = bulk_price + retail_price

            return BuyItem(name=item_name, total=total, bulk=bulk)

        total = sale_item.get('price') * bulk
        return BuyItem(name=item_name, total=total, bulk=bulk)

    @classmethod
    def get_total_prices(cls, list_item: list[BuyItem]) -> Cart:
        item_price = py_.map(list_item, "total")
        cart_total = sum_(item_price)

        return Cart(total=cart_total, items=list_item)

    def get_give_away_info(self, item: BuyItem, buy_date: datetime) -> dict:
        list_give_away = py_.map(self.give_away_product,
                                 lambda give_away: self.get_total_give_away(give_away=give_away, item=item,
                                                                            buy_date=buy_date))
        return py_.filter(list_give_away, lambda give_away: give_away)

    def get_total_give_away(self, give_away: dict, item: BuyItem, buy_date: datetime) -> dict:
        if give_away["product"] == item.name and give_away["day_start"] <= buy_date <= give_away["day_end"]:
            total = item.bulk // give_away["buy"] ** give_away["deal"]
            return {"item": give_away["give_away"], "total": total}
        return None
