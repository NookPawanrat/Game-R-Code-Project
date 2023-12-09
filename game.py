import db_functions as db


class Game:

    id= 1
    def __init__(self, player):
        self.player = player
        self.countries_togo = db.start_game()
        self.crime_location = self.countries_togo[-1]
        self.id= Game.id
        Game.id += 1

    def get_available_countries(self):
        return db.get_available_countries()
    def get_hint(self, player):
        return self.countries_togo[player.correct]['hint']

    def get_answer(self):
        return self.countries_togo[self.player.correct]['name']

    def crime_move(self):
        new = db.update_crime_location()
        self.countries_togo.append(new)
        self.crime_location = new

    def mission_left(self):
        left = len(self.countries_togo) - self.player.correct
        return left

    def mission_fail(self):
        return self.player.life == 0

    def if_win(self):
        return self.player.correct == len(self.countries_togo)

    def criminal_escaped(self):
        return len(self.countries_togo) == 9
