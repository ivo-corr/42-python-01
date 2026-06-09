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
    print("=== Plant Factory Output ===")
    plants = [
        Plant("ROSE", 25, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in plants:
        print(f"Created: {plant.name}: {plant.height}cm,"
              f" {plant.aage} days old")
