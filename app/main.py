class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        if person.get("name") not in Person.people:
            Person(person.get("name"), person.get("age"))

    for person in people:
        method_person = Person.people[person["name"]]
        if person.get("husband") is not None:
            method_person.husband = Person.people[person["husband"]]
        if person.get("wife") is not None:
            method_person.wife = Person.people[person["wife"]]

    return [Person.people[person["name"]] for person in people]
