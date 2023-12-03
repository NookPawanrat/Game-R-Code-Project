from flask import Flask, render_template
import db_functions as db

app = Flask(__name__)


@app.route('/countries')
def index():
    data = [{"nombre": "Reino Unido", "lat": 51.509865, "long": -0.118092},
                 {"nombre": "Argentina", "lat": -34.611778, "long": -58.417309},
                 {"nombre": "Tailandia", "lat": 13.756331, "long": 100.501765},
                 {"nombre": "Egipto", "lat": 30.033, "long": 31.233},
                 {"nombre": "Australia", "lat": -25.274398, "long": 133.775136},
                 {"nombre": "Brasil", "lat": -14.235004, "long": -51.92528},
                 {"nombre": "China", "lat": 35.86166, "long": 104.195397}]
    return render_template('countries.html', data= data)


if __name__ == '__main__':
    app.run(debug=True)
