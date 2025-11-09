# Наследование


# Родительский класс\Супер класс
# class Hero:
#     def __init__(self, name, lvl, hp):
#         # Атрибуты класса
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def action(self):
#         return self.name
#
#
# class Skill:
#     pass
#
#
# # Дочерний класс
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#
#     def action(self):
#         return f"Я потомок {self.name}"
#
#
# class WarriorHero(MageHero):
#     pass
#
#
# obj_1 = Hero("Олег", 10, 100)
# obj_2 = MageHero("Ardager", 100, 1000)
# obj_3 = WarrioHero("Ardager", 100, 1000)
#
# print(obj_1.action())
# print(obj_2.action())




#
# class A:
#
#     def action(self):
#         return "A"
#
# class B(A):
#
#     def action(self):
#         return "B"
#
# class C(A):
#
#     def action(self):
#         return "C"
#
# class D(C, B):
#
#     def action(self):
#         return "D"
#
#
# obj_4 = D()
#
# print(D.__mro__)
#
# print(obj_4.action())


class Animal:
    def action(self):
        return "Animal"

class Fly(Animal):

    def actoin(self):
        return f"Fly"

class Swim(Animal):
    def action(self):
        return "Swim"

class Duck(Swim, Fly):
    ...

duck = Duck()

print(duck.action())



