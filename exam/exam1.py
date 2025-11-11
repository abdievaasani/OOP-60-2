from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Hero:
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self) -> str:
        return f"{self.name} готов к бою!"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Hero):
            return NotImplemented
        return self.name == other.name and self.lvl == other.lvl

class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self) -> str:
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self) -> str:
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    bank_name = "Simba" # атрибут класса
    def __init__(self, hero: Hero, balance: int, password: str):
        self.hero = hero
        self._balance = balance # защищённый атрибут
        self.__password = password # приватный атрибут

    def login(self, password: str) -> bool:
        return password == self.__password

    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name} ({self.hero.__class__.__name__}) | Баланс: {self._balance} SOM | Банк: {self.bank_name}"

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @staticmethod
    def bonus_for_level(lvl: int) -> int:
        return lvl * 10

    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other: "BankAccount") -> int:
        if not isinstance(other, BankAccount):
            return NotImplemented

        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        raise TypeError("Нельзя складывать балансы: герои разных классов")

class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone: str) -> str:
        pass


class KGSms(SmsService):
    def send_otp(self, phone: str) -> str:
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone: str) -> str:
        return f"{{\"text\": \"Код: 1234\", \"phone\": \"{phone}\"}}"

if __name__ == "__main__":
    merlin = MageHero(name="Merlin", lvl=70, hp=900, mp=150)
    conan = WarriorHero(name="Conan", lvl=50, hp=1200, mp=0)

    print(merlin.action())
    print(conan.action())

    acc1 = BankAccount(hero=merlin, balance=5000, password="s3cret")
    acc2 = BankAccount(hero=conan, balance=3000, password="sword")

    print(str(acc1))
    print(str(acc2))

    print(f"Банк: {BankAccount.get_bank_name()}")  # Банк: Simba
    print(f"Бонус за 50 уровень: {BankAccount.bonus_for_level(50)} SOM")

    acc3 = BankAccount(hero=MageHero("Gandalf", 80, 1000, 200), balance=7000, password="staff")
    print("Сумма балансов двух магов:", acc1 + acc3)
    try:
        total = acc1 + acc2
    except TypeError as e:
        print("Сложение аккаунтов мерлина и кона-на:", e)

    merlin_clone = MageHero(name="Merlin", lvl=70, hp=1, mp=1)
    print("Merlin == Merlin clone?", merlin == merlin_clone)

    kg_sms = KGSms()
    ru_sms = RUSms()
    print(kg_sms.send_otp("+996777123456"))
    print(ru_sms.send_otp("+79991234567"))



