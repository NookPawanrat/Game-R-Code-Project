from flask import Flask, render_template, request, redirect
import json
import db_functions as db

app = Flask(__name__)

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

@app.route('/countries')
def index():
    return render_template('countries.html')

@app.route('/get_countries')
def get_countries():
    return db.get_available_countries()

if __name__ == '__main__':
    app.run(debug=True)
