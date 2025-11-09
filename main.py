# Класс
class GameCharacter:
    # Конструктор класса
    def __init__(self, name, level, health):
        # Атрибуты класса self.name = name
        self.level = level
        self.health = health

    def describe(self):
        return f"{self.name} — уровень {self.level}, здоровье: {self.health} HP."

    def level_up(self):
        self.level += 1
        self.health += 20
        print(f"{self.name} повысил уровень! Теперь уровень {self.level} и здоровье {self.health} HP.")
# Oбъект\экземпляр класса
hero1 = GameCharacter("Арина", 5, 100)
hero2 = GameCharacter("Лео", 3, 80)

print(hero1.describe())
hero1.level_up()
print(hero1.describe())

