class Game:
    def __init__(self, player, countries_togo):
        self.player = player
        self.countries_togo = countries_togo
        self.crime_location = countries_togo[-1]
