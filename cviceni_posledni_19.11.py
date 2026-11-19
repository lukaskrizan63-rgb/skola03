
class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    @property
    def jmeno(self):
        return self.__jmeno

    @property
    def telefon(self):
        return self.__telefon

    @property
    def email(self):
        return self.__email

    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.replace(" ", "").isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("Jmeno muze obsahovat pouze pismena")

    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isnumeric():
            self.__telefon = hodnota
        else:
            raise InvalidData("Cislo muze obsahovat pouze cislice")

    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("Email musi obsahovat @")

        if "." not in hodnota:
            raise InvalidData("Email musi obsahovat tecku")

        if hodnota.replace("@", "").replace(".", "").isalnum():
            self.__email = hodnota
        else:
            raise InvalidData("Email musi obsahovat pouze pismena a cislice")

    def __str__(self):
        return f"Osoba: ({self.jmeno}), ({self.telefon}), ({self.email})"

    def __repr__(self):
        return f"Osoba: ({self.jmeno}), ({self.telefon}), ({self.email})"

    @classmethod
    def load_json_data(cls, data):
        osoby = []

        for osoba in data:
            nova_osoba = cls(
                osoba["jmeno"],
                osoba["telefon"],
                osoba["email"]
            )
            osoby.append(nova_osoba)

        return osoby


if __name__ == "__main__":

    data = [
        {
            "jmeno": "Jan Novak",
            "telefon": "123456789",
            "email": "jan@novak.cz"
        },
        {
            "jmeno": "Tomas Novotny",
            "telefon": "987654321",
            "email": "tomas@gmail.com"
        }
    ]

    osoby = Osoba.load_json_data(data)

    print(osoby)
