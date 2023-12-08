import db_functions as db


class Player:

    player_id = 1

    def __init__(self, name):
        self.name = name
        self.location = "Base"
        self.id = Player.player_id
        self.correct = 0
        self.lives = 5
        Player.player_id += 1

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def set_location(self, new_location):
        self.location = new_location

    def get_id(self):
        return self.id

    def get_correct_answer(self):
        return self.correct

    def set_correct_answer(self, answer):
        self.correct += answer

    def get_incorrect_answer(self):
        return 5 - self.lives

    def get_lives(self):
        return self.lives

    def set_lives(self, live):
        self.lives -= live