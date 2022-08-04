class FrozenClass:
    def _freeze(self):
        self.__isfrozen = True


class Technic(FrozenClass):
    budget_item = []
    expensive_goods = []

    def tech(self, product_name,summa,status):
        if summa <= 10000:
            Technic.budget_item.append(product_name)

        else:
            Technic.expensive_goods.append(product_name)

        self._freeze()