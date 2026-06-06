class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    @classmethod
    def anonymous_plant(cls) -> None:
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def age_check(age: int) -> bool:
        if (age > 365):
            return True
        else:
            return False

    def show(self) -> None:
        self.Stats.incr_show()
        print(self._name + ":", self.get_height(), "cm,",
              self.get_age(), "days old")

    def grow(self) -> None:
        self.Stats.incr_grow()
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self.Stats.incr_age()
        self._age = self._age + 1

    def set_height(self, height: int) -> None:
        if (height > 0):
            self._height = height
            print("Height updated:", self._height, "cm")
        else:
            print(self._name + ": Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if (age > 0):
            self._age = age
            print("Age updated:", self._age, "days old")
        else:
            print(self._name + ": Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> int:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


class Flower(Plant):
    class Stats:
        _grow = 0
        _age = 0
        _show = 0

        @classmethod
        def incr_grow(cls):
            cls._grow = cls._grow + 1

        @classmethod
        def incr_age(cls):
            cls._age = cls._age + 1

        @classmethod
        def incr_show(cls):
            cls._show = cls._show + 1

        @classmethod
        def display(cls):
            print("Stats:", cls._grow, "grow,", cls._age,
                  "age,", cls._show, "show")

    def __init__(self, name: str, age: int, height: int, color: str) -> None:
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


class Seed(Flower):
    def __init__(self, name: str, age: int, height: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, age, height, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print("Seeds: " + self._seeds)


class Tree(Plant):
    def __init__(self, name: str, age: int, height: int,
                 diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter

    def produce_shade(self) -> None:
        self._producing_shade = True
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", self._trunk_diameter, "cm")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: int,
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
    p1.Stats.display()
