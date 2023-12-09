from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import game as g
import player as p

app = Flask(__name__)

game = None
player = None

@app.errorhandler(Exception)
def handle_error(error):
    print(f"An error occurred: {str(error)}")
    return redirect("/", code=302)


@app.route("/", endpoint='home')
def home():
    return render_template("start.html", url_home=url_for('home'), url_detective_name=url_for('detective_name'))

@app.route("/get_data", methods=["GET"])
def get_data():
    data = {"full_life": 5, "left_life": player.get_lives()}
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/detective_name', endpoint='detective_name')
def detective_name():
    return render_template('detective_name.html', url_intro='intro')

@app.route('/set_name', methods=["POST"], endpoint='set_name')
def set_detective_name():
    name = request.form["name"]
    global player
    player = p.Player(name.title())
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
            return redirect("/correct")
        else:
            return redirect("/incorrect")

@app.route("/correct")
def correct():
    global player
    player.set_answer(1)
    with open('answer.json', 'r') as file:
        data = json.load(file)
    c_title = data[0]["correct"]["title"]
    c_text = data[0]["correct"]["text"]
    c_button = data[0]["correct"]["button"]
    c_color = data[0]["correct"]["color"]
    c_to = data[0]["correct"]["to"]
    if game.if_win():
        return redirect("/win")
    return render_template("answer.html", title=c_title, text=c_text, color=c_color, to=c_to, button=c_button, name=player.get_name())


@app.route("/incorrect")
def wrong():
    global player
    global game
    player.set_lives(1)
    #game.crime_move()
    with open('answer.json', 'r') as file:
        data = json.load(file)
    i_title = data[0]["incorrect"]["title"]
    i_text = data[0]["incorrect"]["text"]
    i_button = data[0]["incorrect"]["button"]
    i_color = data[0]["incorrect"]["color"]
    i_to = data[0]["incorrect"]["to"]
    if game.criminal_escaped() or player.get_lives() == 0:
        return redirect("/lose")
    return render_template("answer.html", title=i_title, text=i_text, color=i_color, to=i_to, button=i_button)

@app.route("/win")
def win():
    with open('answer.json', 'r') as file:
        data = json.load(file)
    w_title = data[0]["win"]["title"]
    w_text = data[0]["win"]["text"]
    w_button = data[0]["win"]["button"]
    w_color = data[0]["win"]["color"]
    w_to = data[0]["win"]["to"]
    return render_template("answer.html", title=w_title, text=w_text, color=w_color, to=w_to, button=w_button)

@app.route("/lose")
def lose():
    with open('answer.json', 'r') as file:
        data = json.load(file)
    l_title = data[0]["lose"]["title"]
    l_text = data[0]["lose"]["text"]
    l_button = data[0]["lose"]["button"]
    l_color = data[0]["lose"]["color"]
    l_to = data[0]["lose"]["to"]
    return render_template("answer.html", title=l_title, text=l_text, color=l_color, to=l_to, button=l_button)


@app.route("/countries")
def showcountries():
    global game
    countries = game.get_available_countries()
    return render_template("country.html", data=countries)

@app.route('/exit')
def if_exit():
    return render_template("exit.html")

@app.route('/close_session')
def close_session():
    global player
    global game
    player = None
    game = None
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
