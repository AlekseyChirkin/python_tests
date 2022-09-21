class MyFirstClass:
    pass


class Person:

    human = True
    TwoLegs = True

    def __init__(self, name: str, year: int, grade: int):
        self.name = name


object_of_my_class = MyFirstClass()
print(type(object_of_my_class))

student1 = Person('Vasya', 1986, 5)
student2 = Person('Kolya', 2000, 3)
print(student1.name)
print(student2.name)

print(student2.TwoLegs)
print(Person.TwoLegs)