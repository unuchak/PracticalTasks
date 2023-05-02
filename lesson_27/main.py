class Tarelca:

    def __init__(self) -> None:
        super().__init__()
        self.color = "Write"
        self.products = []

    def add(self, product):
        self.products.append(product)

    def info(self):
        return f"Я Тарелочка {self.color}, во мне {len(self.products)}"


class Cotletca:

    def __init__(self, size="Big") -> None:
        super().__init__()
        self.size = size

    def info(self):
        return f"котлетка: {self.size}"


class Ogurechic:

    def __init__(self) -> None:
        super().__init__()
        self.color = "green"

    def info(self):
        return f"огуречек: {self.color}"


def main():
    tarelca = Tarelca()
    cotletca_1 = Cotletca()
    cotletca_2 = Cotletca(size="smoll")
    ogurechic_1 = Ogurechic()

    tarelca.add(cotletca_1)
    tarelca.add(cotletca_2)

    tarelca.add(ogurechic_1)
    tarelca.add(ogurechic_1)

    msg = tarelca.info()

    print(msg)


if __name__ == '__main__':
    main()
