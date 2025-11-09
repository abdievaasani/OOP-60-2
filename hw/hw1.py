# Класс
class Car:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    # Методы
    def description(self):
        return f"Машина: {self.name}, возраст: {self.age} лет, скорость: {self.speed} км\ч"

    def accelerate(self, value):
        self.speed += value
        return f"Скорость машины {self.name} увеличена до {self.speed} км\ч"

# Объекты или экземпляр
car1 = Car("Toyota", 1,100)
car2 = Car("BMW", 5, 130)

print(car1.description())
print(car1.accelerate(30))

print(car2.description())
print(car2.accelerate(50))
