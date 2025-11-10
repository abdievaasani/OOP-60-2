from typing import List

class Animal:
    def __init__(self, name:str, age:int, health:int):
        self.name = name
        self.age = age
        self.health = health

    def info(self)->str:
        return f"{self.name}, {self.age} лет здоровье {self.health}"

    def use_ability(self)-> str:
        return f"{self.name} использует базовую способность"


class Flyable:
    def use_ability(self)-> str:
        base = super().use_ability()
        return f"{base} летает."

class Swimmable:
    def use_ability(self) -> str:
        base = super().use_ability()
        return f"{base} плавает."

class Invisible:
    def use_ability(self) -> str:
        base = super().use_ability()
        return f"{base} становится невидимым."


class Duck(Flyable, Swimmable, Animal):
    pass


class Bat(Flyable, Invisible, Animal):
    pass


class Frog(Swimmable, Animal):
    pass


class Phoenix(Flyable, Invisible, Animal):
    def reborn(self) -> str:
        self.health = max(self.health, 100)
        return f"{self.name} возрождается из пепла! Здоровье теперь {self.health}."

class Zoo:
    def __init__(self):
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)

    def show_all(self) -> None:
        for a in self.animals:
            print(a.info())

    def perform_show(self) -> None:
        for a in self.animals:
            print(a.use_ability())


if __name__ == "__main__":
    zoo = Zoo()
    duck = Duck("Дональд", 5, 40)
    bat = Bat("Бэтти", 5, 50)
    frog = Frog("Кермит", 2, 90)
    phoenix = Phoenix("Феникс", 300, 240)

    for animal in (duck, bat, frog, phoenix):
        zoo.add_animal(animal)

    print("=== Информация о животных ===")
    zoo.show_all()

    print("\n=== Шоу суперспособностей ===")
    zoo.perform_show()

    print("\nMRO для Duck:", Duck.__mro__)
    print("MRO для Phoenix:", Phoenix.__mro__)