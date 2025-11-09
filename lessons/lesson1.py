class Hero:

    def __init__(self, nick_name, lvl, hp):
        self.nick_name = nick_name
        self.lvl = lvl
        self.hp = hp

    # Методы
    def action(self):
        return f"{self.nick_name} Hi this my base action!!"

    # Объекты или экземпляр класса
kirito = Hero("Kirito", 100,10000)
asuna = Hero("Asuna", 100,10000)

print(kirito.action())
print(asuna.action())
