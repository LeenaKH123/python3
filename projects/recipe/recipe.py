import webbrowser
class Ingredient:
    def __init__( self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        print(f"oops, these {self.name} went bad ...")
        self.name = "expired" + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        return Ingredient(name=new_name, amount=1)

    def get_info(self):
        wiki_url = "https://en.wikipedia.org/wiki/"+self.name
        print(wiki_url)
        webbrowser.open(wiki_url)



    def __str__(self):
        return f"{self.name} ({self.amount})"

    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

# i = Ingredient("peas", 2)
# print(i)
# print(repr(i))
# c = Ingredient("carrot", 5)
p = Ingredient("pea", 4)
# s = c.__add__(p)
r = p.get_info()
# print(s)  # OUTPUT: carrotpea (1)

