from pydash import py_


class SuperMarket:
    products = [
        {"name": "coca", "price": 0.5, "bulk": 20, "bulk_price": 9},
        {"name": "rau_diep_ca", "price": 0.5, "bulk": 20, "bulk_price": 9},
    ]

    def get_item_price(self, item_name: str, bulk: int):
        sale_item = py_.find(self.products, lambda item: item.get('name') == item_name)

        if bulk == sale_item.get("bulk"):
            total = sale_item.get("bulk_price")
            return {'name': item_name, "total": total}

        if bulk > sale_item.get("bulk"):
            item_bulk = sale_item.get("bulk")
            price = sale_item.get("bulk_price")
            item_price = sale_item.get("price")

            bulk_price = bulk // item_bulk * price
            retail_price = bulk % item_bulk * item_price
            total = bulk_price + retail_price

            return {'name': item_name, "total": total}

        total = sale_item.get('price') * bulk
        return {'name': item_name, "total": total}


