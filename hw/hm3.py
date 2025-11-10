
import random
from abc import ABC, abstractmethod

# BankAccount (инкапсуляция)
class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name                 # открытый
        self._balance = balance          # защищённый
        self.__password = password       # приватный


    def __check_password(self, password):
        return password == self.__password

    def deposit(self, amount, password):
        if not self.__check_password(password):
            return "Неверный пароль!"
        if amount < 0:

            return "Сумма должна быть положительной!"
        self._balance += amount
        return self._balance

    def withdraw(self, amount, password):
        if not self.__check_password(password):
            return "Неверный пароль!"
        if amount < 0:
            return "Сумма должна быть положительной!"
        if amount > self._balance:
            return "Недостаточно средств!"
        self._balance -= amount
        return self._balance

    def change_password(self, old_password, new_password):
        if not self.__check_password(old_password):
            return "Старый пароль неверный"
        self.__password = new_password
        return "Пароль изменён"

    def get_balance(self, password):
        if not self.__check_password(password):
            return "Неверный пароль!"
        return self._balance

    def reset_pin(self, password):
        if not self.__check_password(password):
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return new_pin

    def __generate_pin(self):
        value = random.randint(0, 9999)
        return f"{value:04d}"

#2
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

    def get_service(self):
        return f"Сервис: {self._service}"


class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    def send(self, message, recipient):
        return f"Email sent to {recipient}"


class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"


class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"


#3– Система входа и переводов:
class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        is_ok = isinstance(self.account.get_balance(password), (int, float))
        if is_ok:
            print(self.notifier.send(f"Успешный вход: {self.username}", "system"))
            return True
        return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        if not isinstance(self.account.get_balance(password), (int, float)):
            return "Неверный пароль!"

        result = self.account.withdraw(amount, password)
        if isinstance(result, str):
            return result

        recipient_account._balance += amount  # как указано в задании

        # Уведомления
        print(self.notifier.send(f"Перевод {amount} отправлен", "system"))
        print(self.notifier.send(f"Получено {amount} от {self.username}", "system"))

        return f"Перевод успешен. Новый баланс: {self.account._balance}"

if __name__ == "__main__":
    print("=== Тест BankAccount ===")
    acc = BankAccount("Tester", 200, "123qwerty")
    print(acc.deposit(50, "123qwerty"))         # 250
    print(acc.withdraw(100, "123qwerty"))       # 150
    print(acc.get_balance("123qwerty"))         # 150
    print(acc.change_password("wrong", "new"))  # "Старый пароль неверный"
    print(acc.change_password("123qwerty", "new"))  # "Пароль изменён"


    random.seed(11316)
    print(acc.reset_pin("new"))                 # 5832
    print(acc.get_balance("5832"))              # 150

    print("\n=== Тест NotificationSender ===")
    email = EmailSender()
    print(email.send("Привет", "test@mail.ru"))
    print(email.get_service())
    sms = SmsSender()
    print(sms.get_service())

    print("\n=== Тест UserAuth ===")
    john = BankAccount("John", 150, "secret")
    alice = BankAccount("Alice", 50, "pass123")
    notifier = SmsSender()
    auth = UserAuth("john_doe", john, notifier)

    auth.login("secret")  # печатает "SMS sent to system"
    print(auth.transfer(70, "secret", alice))
    print(f"John balance: {john._balance}")
    print(f"Alice balance: {alice._balance}")
