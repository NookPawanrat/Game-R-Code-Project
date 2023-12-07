from flask import Flask, render_template, request, redirect, url_for
import json
import game
import player as p

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("start.html")


@app.route('/detective_name')
def detective_name():
    return render_template('detective_name.html')


@app.route('/set_name', methods=["POST"])
def set_detective_name():
    name = request.form["name"]
    p.name(name)
    return redirect('/intro')


@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route("/intro")
def intro():
    return render_template("intro.html")

@app.route("/file")
def file():
    return render_template("mission-file.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/answer", methods=['POST'])
def answer():
    if request.method == 'POST':
        ans = request.form["answer"]
        if ans == "correct":
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("wrong"))


# we could render our win/lose template here
@app.route("/answercorrect")
def correct():
    return render_template("correct.html", name="sherlock", country="Finland", failTimes="5", missionLeft="5")


@app.route("/answerwrong")
def wrong():
    return render_template("incorrect.html")


@app.route("/countries")
def showcountries():
    country = [{'name': 'Argentina'},{'name': 'Brazil'}, {'name': 'China'}]
    return render_template("country.html", data = country)


@app.route('/get_countries')
def get_countries():
    return db.get_available_countries()


@app.route('/exit')
def if_exit():
    return render_template("exit.html")

if __name__ == '__main__':
    app.run(debug=True)
