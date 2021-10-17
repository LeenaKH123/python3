class Ingredient:
    def __init__( self, name):
        self.name = name

    def expire(self):
        print(f"oops, these {self.name} went bad ...")
        self.name = "expired" + self.name

i = Ingredient("peas")
print(i.name)  # OUTPUT: peas
i.expire()
print(i.name)  # OUTPUT: expired peas
print(i.name)  # OUTPUT: expired peas