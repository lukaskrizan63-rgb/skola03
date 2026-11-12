
class Vektor:
    def __init__(self, tmp_x, tmp_y):
        self.x = tmp_x
        self.y = tmp_y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def secti(self, jiny_vektor):
        return Vektor(self.x + jiny_vektor.x,
                      self.y + jiny_vektor.y)

    def vynasob(self, skalar):
        return Vektor(self.x * skalar,
                      self.y * skalar)


if __name__ == "__main__":
    v1 = Vektor(10, 5)
    print(v1)

    v2 = Vektor(3, 8)
    print(v1.secti(v2))

    print(v2.vynasob(2))
