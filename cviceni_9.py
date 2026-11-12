
class ChybnaCastka(Exception):
    pass


class BankovniUcet:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.__zustatek = 0

    def __str__(self):
        return f"Muj ucet ({self.jmeno}) ma {self.__zustatek} kc"

    def vloz(self, castka):
        # Vlozit jde pouze kladna castka
        if castka <= 0:
            raise ChybnaCastka("Castka musi byt kladna")
        self.__zustatek += castka

    def vyber(self, castka):
        # Vybrat lze pouze kladnou castku nizsi nez zustatek
        if castka <= 0 or castka > self.__zustatek:
            raise ChybnaCastka("Neplatna castka pro vyber")
        self.__zustatek -= castka

    def pripis_uroky(self):
        # Navysi zustatek uctu o nasobek uroku
        self.__zustatek += self.__zustatek * self.urok


if __name__ == "__main__":
    ucet = BankovniUcet("sporici", 0.05)
    ucet.vloz(200)
    ucet.vyber(100)
    ucet.pripis_uroky()
    print(ucet)
