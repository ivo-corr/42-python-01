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
            print(f"Age updated: {self._age} days old")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_name(self) -> str:
        return (self._name)

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


if __name__ == '__main__':
    print("=== Garden Security System ===")
    p1 = Plant("ROSE", 15.0, 10)
    print(f"Plant created: {p1.get_name()}: {p1.get_height()}cm,"
          f" {p1.get_age()} days old")
    print()
    p1.set_height(25)
    p1.set_age(30)
    print()
    p1.set_height(-10)
    p1.set_age(-50)
    print()
    print(f"Current state: {p1.get_name()}: {p1.get_height()}cm,"
          f" {p1.get_age()} days old")
