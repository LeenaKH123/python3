class Dog:
    kind = [
        "canine"
    ]  # this is true for mutable variables (lists, dict, classes, sets??)

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print(d.tricks)
print(e.tricks)
e.name = "lina"
print(e.name)
d.kind.append("new name")
print(d.kind)
print(e.kind)
