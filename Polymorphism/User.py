"""
1. Написать класс User, у него будут в конструкторе определяться поля age, name, user_type,
а метод будет access_database.
2. Сделать метод таким, чтобы если self.user_type был равен “superuser”, то метод выводил в
консоль “access granted”, в случае если это просто юзер, то выводило “access denied”.
3. Для суперюзера сделать унаследованный класс SuperUser от User
"""


class User:
    """
    class User
    :param name: str. Example: "Olga"
    :param age: int. Example: 25
    :param user_type: user
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.user_type = "user"

    def access_database(self):
        """
        Выводит "access denied" для user_type == user
        """
        if self.user_type == "superuser":
            print("access granted")
        elif self.user_type == "user":
            print("access denied")
        else:
            print("Type user Error, type_user should be = user or superuser")


class SuperUser(User):
    """
    class SuperUser
    :param name: str. Example: "Olga"
    :param age: int. Example: 25
    :param user_type: user / superuser
    """
    def __init__(self, name, age):
        super().__init__(name, age)
        self.user_type = "superuser"




# Test access_database  -> Lilia - User -> access granted, Olga - SuperUser -> access granted
print("Test access_database")
lilia = User("Lilia", 30)
lilia.access_database()
olga = SuperUser("Olga", 25)
olga.access_database()
print("    ")

# Test access_database -> Type user Error
print ("="*10)
print("Test Type user Error")
katia = SuperUser("Katia", 30)
katia.access_database()
