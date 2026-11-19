
class ZapornyZustatek(Exception):
    pass


class BankovniUcet:
    def __init__(self):
        self.__zustatek = 0

    @property
    def zustatek(self):
        return self.__zustatek

    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0:
            raise ZapornyZustatek("Nelze nastavit zaporny zustatek")
        self.__zustatek = hodnota


if __name__ == "__main__":

    u = BankovniUcet()

    print(u.zustatek)

    u.zustatek = 100

    print(u.zustatek)
