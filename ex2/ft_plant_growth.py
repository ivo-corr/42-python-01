class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_ = age

    def show(self):
        print(self.name + ":", self.height, "cm,", self.age_, "days old")

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age(self):
        self.age_ = self.age_ + 1


if __name__ == '__main__':
    random_plant = Plant("ROSE", 25, 30)
    print("=== Garden Plant Growth ===")
    for i in range(7):
        print("=== Day", (i + 1), "===")
        random_plant.grow()
        random_plant.age()
        random_plant.show()
        i = i + 1
