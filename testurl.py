from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", endpoint='home')
def home():
    return render_template("urls.html", url_home=url_for('home'), url_dashboard=url_for('dashboard'))


@app.route("/dashboard", endpoint='dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
