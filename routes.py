from flask import Flask, render_template, request, redirect, url_for
import json
import db_functions as db

app = Flask(__name__)


@app.route("/", endpoint='home')
def home():
    return render_template("start.html", url_home=url_for('home'), url_detective_name=url_for('detective_name'))

@app.route('/detective_name', endpoint='detective_name')
def detective_name():
    return render_template('detective_name.html',url_intro='intro')

@app.route('/set_name', methods=["POST"], endpoint='set_name')
def set_detective_name():
    name = request.form["name"]
    db.set_player_name(name)
    return redirect('/intro')

@app.route('/intro', endpoint='intro')
def intro():
    return render_template('intro.html', url_mission_file='mission_file', url_howtoplay='howtoplay')

@app.route('/mission_file', endpoint='mission_file')
def mission_file():
    return render_template("mission-file.html",url_dashboard='dashboard')

@app.route("/howtoplay", endpoint='howtoplay')
def howtoplay():
    return render_template("howto.html")

@app.route("/dashboard", endpoint='dashboard')
def dashboard():
    return render_template("dashboard.html", playerName=p.name, playerNumber=p.id, country=p.current_location,
                           hint=test.visited_location[0]["hint"], missionLeft=len(test.visited_location)-test.solved)


@app.route("/answer", methods=['POST'])
def answer():
    if request.method == 'POST':
        ans = request.form["answer"]
        if ans == test.visited_location[0]["name"]:
            return redirect(url_correct = url_for('correct'))
        else:
            return redirect(url_correct = url_for('wrong'))


# we could render our win/lose template here
@app.route("/answercorrect", endpoint='correct')
def correct():
    return "Congratulations! Your answer is correct!"


@app.route("/answerwrong", endpoint='wrong')
def wrong():
    return "Sorry, your answer is wrong."



@app.route("/countries", endpoint='countries')
def showcountries():
    return render_template("countries.html")


#Do we need get_counties()??
@app.route('/get_countries', endpoint='get_countries')
def get_countries():
    return db.get_available_countries()


if __name__ == "__main__":
    app.run(debug=True)


