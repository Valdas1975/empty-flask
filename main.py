import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query = 'Vilnius'
    unit = 'metric'
    api_key = '67df05bf49a50660e115606f8eede5bb'

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)

    data = requests.get(url=url).json()

    items = range(0, 10)

    return render_template('index2.html',
        data=data,
        items=items
    )

@app.route("/login", methods=["POST"])
def login():
    # Logino funkcija
    return render_template('index.html')

@app.route("/logout", methods=["POST"])
def logout():
    # Logouto funkcija
    return render_template('index.html')

@app.route("/send-message", methods=["POST"])
def send_message():
    # Zinutes siuntimas

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
