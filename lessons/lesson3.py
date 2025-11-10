# Инкапсуляция и Абстракция
# import random
# import string
# from unittest.mock import magic_methods
#
# class BankAccount:
#     def __init__(self, name, balance, password):
#         self.name = name   # Открытая атрибута
#         self._balance = balance # Защищенная атрибута
#         self.__password = password # Приватная атрибута
#
#     def login(self, password):
#         if self.__password == password:
#             print("Вы вошли!!")
#         else:
#             print("Не верный пароль!!")
#
#
#     def get_balace(self, password):
#         if self.__password == password:
#             return self._balance
#         else:
#             return "не верный пароль!!"
#     def __random__pass(self):
#         chart = string.ascii_letters + string.digits
#         password = ''.join(random.choice(chart)for _ in range(6))
#         return password
#
#     def get_new_pass(self):
#         return self.__random_pass()
#
#
#
# john = BankAccount("John", 100,"123qwerty")
#
# john.login("12345")
# print((john.get_balace("123qwerty")))
# print((john.get_new_pass()))









class Animal(ABC)