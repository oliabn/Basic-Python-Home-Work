class Person:
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
    def __init__(self):
        self._person_list = []

    @staticmethod
    def is_match(criterion, person):
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

    def is_complete_match(self, person, criteria):
        """
        Совпадает ли персона по всем искомым критериям?
        :param person: Person Example ("Sergiush", 31, "man", "Poland", 175, 90)
        :param criteria: Example {"age": 31, "country": "Poland"}
        :return: True/False
        """
        for criterion in criteria.items():
            if self.is_match(criterion, person):
                pass
            else:
                return False
        return True

    def read_data(self, criteria):      # criteria = {"age": 31, "country": "Poland"} -> [("age", 31), ("country": "Poland")]
        sought_person = []
        if len(criteria) == 0:
            print("Error")
            return []

        for person in self._person_list:
            if self.is_complete_match(person, criteria):
                sought_person.append(person)
        return sought_person

    def write_data(self, person):
        self._person_list.append(person)


def test_is_match():
    database = Database()
    sergiush = Person("Sergiush", 31, "man", "Poland", 175, 90)
    database.write_data(sergiush)
    criteria = ("age", 31)

    expected = True
    found = database.is_match(criteria, sergiush)

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
