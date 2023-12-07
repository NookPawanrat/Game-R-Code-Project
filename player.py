import db_functions as db

class Player:

    player_id= 1

    def __init__(self):
        self.player_name = name
        self.location = "Base"
        self.id = Player.player_id
        self.correct_answers = 0
        self.lives = 5
        Player.player_id += 1

    @name
    def set_name(self, player_name):
        db.set_player_name(player_name)
        self.player_name= player_name
    @name
    def get_name(self):
        return self.name

    @location
    def location(self, location):
        self.location = location

    @location
    def location(self):
        return self.location

    @id
    def get_id(self):
        return self.id

    @correct_answer
    def get_correct_answer(self):
        return self.correct_answers

    @correct_answer
    def set_correct_answer(self, answer):
        self.correct_answers += answer

    @incorrect_answer
    def get_incorrect_answer(self):
        return 5 - self.lives

    @lives
    def get_lives(self):
        return self.lives

    @lives
    def set_lives(self, live):
        self.lives -= live