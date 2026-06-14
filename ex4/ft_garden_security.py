#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        if (height >= 0):
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0
            print(f"{self.name}: Height initialized to default value: 0")
        if (age >= 0):
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            self._age = 0
            print(f"{self.name}: Age initialized to default value: 0")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old ")

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._age = self._age + 1

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._age = age
            print(f"Age updated: {self._age} days old")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


if __name__ == '__main__':
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    print(f"Plant created: {p1.name}: {p1.get_height()}cm,"
          f" {p1.get_age()} days old")
    print()
    p1.set_height(25)
    p1.set_age(30)
    print()
    p1.set_height(-10)
    p1.set_age(-50)
    print()
    print(f"Current state: {p1.name}: {p1.get_height()}cm,"
          f" {p1.get_age()} days old")
