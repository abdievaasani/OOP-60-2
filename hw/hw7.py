import sqlite3
connect = sqlite3.connect('hogwarts_teachers.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers(
    name VARCHAR(20) NOT NULL,
    subject TEXT NOT NULL,
    role TEXT
    )
''')
connect.commit()

def create_teacher(name, subject, role):
    cursor.execute(
        'INSERT INTO teachers(name, subject, role) VALUES(?, ?, ?)',
        (name, subject, role)
    )
    connect.commit()
    print("Учитель добавлен!")

create_teacher("Минерва Макгонагалл", "Трансфигурация", "Заместитель директора")
create_teacher("Северус Снегг", "Зельеварение", "Позже ЗОТИ")
create_teacher("Филиус Флитвик", "Чары", None)
create_teacher("Помона Стебль", "Травология", None)
create_teacher("Рубеус Хагрид", "Уход за магическими существами", None)
create_teacher("Ремус Люпин", "Защита от тёмных искусств", "3 курс")
create_teacher("Долорес Амбридж", "Защита от тёмных искусств", "5 курс")
create_teacher("Альбус Дамблдор", "Директор", "Орден Мерлина")

def read_teachers():
    cursor.execute("SELECT * FROM teachers")
    for teacher in cursor.fetchall():
        print(teacher)


print("\nСписок учителей:")
read_teachers()
connect.close()
