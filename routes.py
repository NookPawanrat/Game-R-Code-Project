from flask import Flask, render_template, request, redirect, url_for
import json
import game as g
import player as p

app = Flask(__name__)

game = None
player = None

@app.route("/", endpoint='home')
def home():
    return render_template("start.html", url_home=url_for('home'), url_detective_name=url_for('detective_name'))

@app.route("/get_data", methods=["GET"])
def get_data():
    data = {"player_name": "Sherlock", "player_id": 1, "player_location": "Finland", "mission_left": 5, "full_life": 5, "left_life": 3}
    return jsonify(data)

@app.route('/detective_name', endpoint='detective_name')
def detective_name():
    return render_template('detective_name.html',url_intro='intro')

@app.route('/set_name', methods=["POST"], endpoint='set_name')
def set_detective_name():
    name = request.form["name"]
    global player
    player = p.Player(name)
    return redirect('/intro')

@app.route('/intro', endpoint='intro')
def intro():
    return render_template('intro.html', url_mission_file='mission_file', url_howtoplay='howtoplay')

@app.route('/mission_file')
def mission_file():
    global game
    global player
    game = g.Game(player)
    return render_template("mission-file.html")

@app.route("/howtoplay")
def howtoplay():
    return render_template("howto.html")

@app.route("/dashboard", endpoint='dashboard')
def dashboard():
    global player
    global game
    player_id = player.get_id()
    player_name = player.get_name()
    player_location = player.get_location()
    missions_left = 5 + player.get_incorrect_answer() - player.get_correct_answer()
    hint = game.get_hint(player)
    return render_template("dashboard.html", url_answer='answer', name=player_name, country=player_location, missions=missions_left, id= player_id, hint= hint)

@app.route("/answer", methods=['POST'], endpoint='answer')
def answer():
    global game
    global player
    if request.method == 'POST':
        ans = request.form["answer"]
        if ans.title() == game.get_answer():
            player.set_location(ans.title())
            return redirect(url_for("correct"))
        else:
            return redirect(url_for('wrong'))


# we could render our win/lose template here
@app.route("/answercorrect")
def correct():
    player.set_answer(1)
    return render_template("correct.html")


@app.route("/answerwrong")
def wrong():
    global player
    global game
    player.set_lives(1)
    #game.crime_move()
    return render_template("incorrect.html")


@app.route("/countries")
def showcountries():
    global game
    countries = game.get_available_countries()
    return render_template("country.html", data=countries)

@app.route('/exit')
def if_exit():
    return render_template("exit.html")


if __name__ == "__main__":
    app.run(debug=True)
