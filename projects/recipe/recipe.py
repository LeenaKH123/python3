class Ingredient:
    def __init__( self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        print(f"oops, these {self.name} went bad ...")
        self.name = "expired" + self.name

    def __str__(self):
        return f"{self.name} ({self.amount})"

    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

i = Ingredient("peas", 2)
print(i)
print(repr(i))

