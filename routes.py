from flask import Flask, render_template, request, redirect, url_for
import json
#import game
#import player as p

app = Flask(__name__)



@app.route("/", endpoint='home')
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
    p.name(name)
    return redirect('/intro')

@app.route('/intro', endpoint='intro')
def intro():
    return render_template('intro.html', url_mission_file='mission_file', url_howtoplay='howtoplay')

@app.route('/mission_file')
def mission_file():
    return render_template("mission-file.html")

@app.route("/howtoplay")
def howtoplay():
    return render_template("howto.html")

@app.route("/dashboard", endpoint='dashboard')
def dashboard():
    return render_template("dashboard.html",url_answer='answer', url_howtoplay='howtoplay', url_countries='countries', url_exit='exit')


@app.route("/answer", methods=['POST'], endpoint='answer')
def answer():
    if request.method == 'POST':
        ans = request.form["answer"]
        if ans == "correct":
            return redirect(url_for("correct"))
        else:
            return redirect(url_for('wrong'))


# we could render our win/lose template here
@app.route("/answercorrect")
def correct():
    return render_template("correct.html")


@app.route("/answerwrong")
def wrong():
    return render_template("incorrect.html")


@app.route("/countries")
def showcountries():
    country = [{'name': 'Argentina'}, {'name': 'Brazil'}, {'name': 'China'}]
    return render_template("country.html", data=country)

@app.route('/exit')
def if_exit():
    return render_template("exit.html")


if __name__ == "__main__":
    app.run(debug=True)
