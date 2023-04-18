"""
Homework from Basic Python
Subject: Abstraction
Task:
1. Организуйте архитектуру приложения “База данных” (псевдо). В роли базы данных у вас
будет класс Database, который будет хранить данные в виде переменной списка.
2. Класс Database должен иметь методы read_data(criteria), write_data(element).
3. Для элемента данных напишите класс Data. В данном случае мы будем хранить данные о
пользователях. Data будет иметь атрибуты: country, name, age, gender, height, weight.
4. В классе Database метод read_data будет принимать на вход аргумент criteria, который
является словарем вида {“age”: 25}, после чего метод вернет отдельный список всех
элементов у которых данное условие истино.
Подсказка: чтобы получить у объекта класса значение его атрибута как у словаря, используйте
следующий синтаксис: your_class_instance.__dict__.get(‘name’).
PS: организуйте правильную инкапсуляцию. Вы должны добавлять элементы в класс Database
только через метод write, но никак не напрямую через атрибут elements
"""


class Person:
    """
    class Person stores data about people: name, age, gender, country, height, weight
    """
    def __init__(self, name, age, gender, country, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}, {self.country}, {self.height}, {self.weight}"


class Database:
    """
    class Database has two public methods:
        - read_data(self, criteria) -> adds people to the list of Person objects
        - write_data(self, person) -> displays people who match the criteria passed to the method
    """
    def __init__(self):
        self._person_list = []

    @staticmethod
    def _is_match(criterion, person):
        """
        Совпадает ли персона по одному критерию
        :param criterion: tulpe. Example: ("age", 31)
        :param person: Person. Example: ("Sergiush", 31, "man", "Poland", 175, 90)
        :return: True/False
        """
        key, value = criterion
        if person.__dict__.get(key) == value:
            return True
        else:
            return False

    def _is_complete_match(self, person, criteria):
        """
        Совпадает ли персона по всем искомым критериям?
        :param person: Person Example ("Sergiush", 31, "man", "Poland", 175, 90)
        :param criteria: Example {"age": 31, "country": "Poland"}
        :return: True/False
        """
        for criterion in criteria.items():
            if self._is_match(criterion, person):
                pass
            else:
                return False
        return True

    def read_data(self, criteria):
        """
        displays people who match the criteria passed to the method
        :param criteria: List Of Touple -> [("age", 31), ("country": "Poland")]
        :return: List sought_person
        """
        sought_person = []
        if len(criteria) == 0:
            print("Error")
            return []

        for person in self._person_list:
            if self._is_complete_match(person, criteria):
                sought_person.append(person)
        return sought_person

    def write_data(self, person):
        """
        adds people to the list of Person objects
        :param person: Person("Ola", 31, "woman", "Poland", 170, 50)
        :return: -
        """
        self._person_list.append(person)


def test_is_match():
    database = Database()
    sergiush = Person("Sergiush", 31, "man", "Poland", 175, 90)
    database.write_data(sergiush)
    criteria = ("age", 31)

    expected = True
    found = database._is_match(criteria, sergiush)

    if found != expected:
        print("Нэ робэ")
    else:
        print("робэ")


def test_empty():
    database = Database()
    ola = Person("Ola", 31, "woman", "Poland", 170, 50)
    lesha = Person("Lesha", 31, "man", "Poland", 170, 60)
    sergiush = Person("Sergiush", 30, "man", "Poland", 175, 90)
    database.write_data(ola)
    database.write_data(lesha)
    database.write_data(sergiush)

    criteria = {"age": 31, "height": 175}

    expected = []
    found = database.read_data(criteria)
    if found != expected:
        print("Нэ робэ")
    else:
        print("робэ")


def test_1():
    database = Database()
    ola = Person("Ola", 31, "woman", "Poland", 170, 50)
    lesha = Person("Lesha", 31, "man", "Poland", 170, 60)
    sergiush = Person("Sergiush", 31, "man", "Poland", 175, 90)
    database.write_data(ola)
    database.write_data(lesha)
    database.write_data(sergiush)

    criteria = {"age": 31, "height": 175}

    expected = [sergiush]
    found = database.read_data(criteria)
    if found != expected:
        print("Нэ робэ")
    else:
        print("робэ")

# test_empty()
# test_1()
# test_is_match()

database = Database()
ola = Person("Ola", 31, "woman", "Poland", 170, 50)
lesha = Person("Lesha", 31, "man", "Poland", 175, 60)
sergiush = Person("Sergiush", 31, "man", "Poland", 175, 90)
database.write_data(ola)
database.write_data(lesha)
database.write_data(sergiush)
criteria = {"age": 31, "height": 175}


for person in database.read_data(criteria):
    print(person)
