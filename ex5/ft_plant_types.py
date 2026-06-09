class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old ")

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._age = self._age + 1

    def set_height(self, height: float) -> None:
        if (height > 0):
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if (age > 0):
            self._age = age
            print("Age updated:", self._age, "days old")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print("Color: " + self._color)
        if (self._bloomed):
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, age: int, height: float,
                 diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter

    def produce_shade(self) -> None:
        self._producing_shade = True
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", self._trunk_diameter, "cm")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print("Harvest season: " + self._harvest_season)
        print("Nutritional value:", self._nutritional_value)

    def grow(self) -> None:
        super().grow()
        self._height = round(self._height + 1.3, 1)
        self._nutritional_value += 1


if __name__ == '__main__':
    print("=== Garden Plant Types ===")
    print("=== Flower")
    p1 = Flower("Rose", 10, 15.0, "red")
    p1.show()
    print("[asking the rose to bloom]")
    p1.bloom()
    p1.show()
    print()
    print("=== Tree")
    p2 = Tree("Oak", 365, 200.0, 5.0)
    p2.show()
    print("[asking the oak to produce shade]")
    p2.produce_shade()
    print()
    print("=== Vegetable")
    p3 = Vegetable("Tomato", 10, 5.0, "April", 0)
    p3.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        p3.grow()
        p3.age()
    p3.show()
