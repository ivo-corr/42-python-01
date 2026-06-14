#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old ")


if __name__ == '__main__':
    print("=== Garden Plant Registry ===")
    random_plant = Plant("Rose", 25, 30)
    random_plant_two = Plant("Sunflower", 80, 45)
    random_plant_three = Plant("Cactus", 15, 120)
    random_plant.show()
    random_plant_two.show()
    random_plant_three.show()
