import db_functions as db


class Game:
    def __init__(self, player, countries_togo):
        self.player = player
        self.countries_togo = countries_togo
        self.crime_location = countries_togo[-1]

    def get_hint(self):
        return self.countries_togo[self.player.correct]['hint']

    def answer_correct(self, answer):
        if answer == self.countries_togo[self.solved]['name']:
            self.player.correct += 1
            return True
        else:
            return False

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

