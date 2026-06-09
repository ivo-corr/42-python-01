class Plant:
    class Stats:
        def __init__(self, grow=0, age=0, show=0):
            self._grow = grow
            self._age = age
            self._show = show

        def incr_grow(self):
            self._grow = self._grow + 1

        def incr_age(self):
            self._age = self._age + 1

        def incr_show(self):
            self._show = self._show + 1

        def display(self):
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age
        self._stats = self.Stats()

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def age_check(age: int) -> bool:
        if (age > 365):
            return True
        else:
            return False

    def show(self) -> None:
        self._stats.incr_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old ")

    def grow(self) -> None:
        self._stats.incr_grow()

    def age(self) -> None:
        self._stats.incr_age()

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
            print(f"Age updated: {self._age} days old")
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
        self._stats = self.Stats()

    def grow(self):
        super().grow()
        self.set_height(self.get_height() + 8)

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(" Color: " + self._color)
        if (self._bloomed):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, age: int, height: float,
                 color: str, seeds: int) -> None:
        super().__init__(name, age, height, color)
        self._seeds = seeds

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def grow(self):
        super().grow()
        self._height = self._height + 22

    def age(self):
        super().age()
        self._age = self._age + 20

    def show(self) -> None:
        super().show()
        print(" Seeds:", self._seeds)


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self, shade=0):
            super().__init__()
            self._shade = shade

        def incr_shade(self):
            self._shade = self._shade + 1

        def display(self):
            super().display()
            print(f" {self._shade} shade")

    def __init__(self, name: str, age: int, height: float,
                 diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter
        self._stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        self._stats.incr_shade()
        self._producing_shade = True
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")

    def show(self) -> None:
        super().show()
        print(" Trunk diameter:", self._trunk_diameter, "cm")


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


def display_statistics(plant: Plant):
    plant._stats.display()


if __name__ == '__main__':
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.age_check(30))
    print("Is 400 days more than a year? ->", Plant.age_check(400))
    print()
    print("=== Flower")
    p1 = Flower("Rose", 10, 15.0, "red")
    p1.show()
    print("[statistics for Rose]")
    display_statistics(p1)
    print("[asking the rose to grow and bloom]")
    p1.grow()
    p1.bloom()
    p1.show()
    print("[statistics for Rose]")
    display_statistics(p1)
    print()
    print("=== Tree")
    p2 = Tree("Oak", 365, 200.0, 5.0)
    p2.show()
    print("[statistics for Oak]")
    display_statistics(p2)
    print("[asking the oak to produce shade]")
    p2.produce_shade()
    print("[statistics for Oak]")
    display_statistics(p2)
    print()
    print("=== Seed")
    p3 = Seed("Sunflower", 45, 80.0, "yellow", 0)
    p3.show()
    print("[make Sunflower grow, age and bloom]")
    p3.grow()
    p3.age()
    p3.bloom()
    p3.show()
    print("[statistics for Sunflower]")
    display_statistics(p3)
    print()
    print("=== Anonymous")
    p4 = Plant.anonymous_plant()
    p4.show()
    print("[statistics for Unknown plant]")
    display_statistics(p4)
