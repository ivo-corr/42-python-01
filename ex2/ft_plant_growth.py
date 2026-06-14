#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.aage = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.aage} days old ")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.aage = self.aage + 1


if __name__ == '__main__':
    initial_height = 25.0
    random_plant = Plant("ROSE", initial_height, 30)
    print("=== Garden Plant Growth ===")
    for i in range(7):
        print(f"=== Day {(i + 1)}===")
        random_plant.show()
        random_plant.grow()
        random_plant.age()
        i = i + 1
    print(f"Growth this week: {round(random_plant.height - initial_height)}cm")
