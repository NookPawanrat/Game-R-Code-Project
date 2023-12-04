from flask import Flask, render_template, request, url_for, redirect
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='crime_game',
    user='root',
    password='123456',
    autocommit=True
)

countries = []
sql = "SELECT country_name, hint FROM hints "
sql += "ORDER BY RAND() LIMIT 5;"
cursor = connection.cursor()
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    country = {"name": result[0], "hint": result[1]}
    countries.append(country)


class Game:
    def __init__(self, player, limit=5):
        # one player object for every game object
        self.player = player
        # how many Ricina can be disposed before player lose the game
        self.limit = limit
        # a list of country objects, randomly generated when game object created
        self.visited_location = countries
        # the last country object in visited_location
        self.crime_location = self.visited_location[-1]
        self.solved = 0

    def set_random_locations(self):
        pass

    def is_correct(self):
        pass

    def update_crime_location(self):
        pass

    def get_hint(self):
        pass

    def is_win(self):
        pass


class Player:
    def __init__(self, player_name, id, current_location='base'):
        self.name = player_name
        self.id = id
        self.current_location = current_location


# use ORM?
class Country:
    def __init__(self, country_name, clue):
        self.name = country_name
        self.clue = clue


p = Player("Sherlock", 1, "base")
test = Game(p)


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", playerName=p.name, playerNumber=p.id, country=p.current_location,
                           hint=test.visited_location[0]["hint"], missionLeft=len(test.visited_location)-test.solved)

@app.route("/answer", methods=['POST'])
def answer():
    if request.method == 'POST':
        ans = request.form["answer"]
        if ans == test.visited_location[0]["name"]:
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("wrong"))


# we could render our win/lose template here
@app.route("/answercorrect")
def correct():
    return "Congratulations! Your answer is correct!"


@app.route("/answerwrong")
def wrong():
    return "Sorry, your answer is wrong."


@app.route("/howtoplay")
def howtoplay():
    return render_template("howto.html")


@app.route("/countries")
def showcountries():
    return render_template("countries.html")


app.run(host="127.0.0.1", debug=True, port=5000)
