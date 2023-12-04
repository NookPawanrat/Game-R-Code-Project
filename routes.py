from flask import Flask, render_template, request, redirect
import json
import db_functions as db
import game

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", playerName=game.p.name, playerNumber=game.p.id, country=game.p.current_location,
                           hint=game.test.visited_location[0]["hint"], missionLeft=len(game.test.visited_location)-game.test.solved)

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
    data = db.get_available_countries()
    return render_template("countries.html", data= data)

@app.route('/detective_name')
def detective_name():
    return render_template('detective_name.html')

@app.route('/set_name', methods=["POST"])
def set_detective_name():
    name = request.form["name"]
    db.set_player_name(name)
    return redirect('/howto')


@app.route('/howto')
def howto():
    return render_template('howto.html')

@app.route('/get_countries')
def get_countries():
    return db.get_available_countries()

if __name__ == '__main__':
    app.run(debug=True)
