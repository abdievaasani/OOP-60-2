class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


def admin_only(func):
    def wrapper(user):
        if user.is_admin == True:
            return func(user)
        else:
            print(PermissionError("Доступ запрещен! Нужны права админа."))
    return wrapper

@admin_only
def delete_database(user):
 print("База данных удалена!")

admin = User("Алексей", is_admin=True)
user = User("Мария", is_admin=False)

# Админ может удалить
delete_database(admin)
# → База данных удалена!

# Обычный пользователь — нет
delete_database(user)
# → PermissionError: Доступ запрещён! Только админ может выполнить эту операцию.




