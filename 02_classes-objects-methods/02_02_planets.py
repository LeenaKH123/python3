# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet:
    season_all = ["autumn", "spring", "winter", "summer"]

    def __init__(self, id, name, distance, season):
        self.name = name
        self.id = id
        self.distance = distance
        self.season = season

    def __str__(self):
        return f"{self.id}, {self.name}, {self.distance}, {self.season}"

    def rotate(self, season_index):
        currentseason = Planet.season_all.index(self.season)
        self.season = Planet.season_all[(currentseason + season_index) % 4]


mars = Planet("1", "mars", "220", "summer")
print(mars)
mars.rotate(1)
print(mars)
