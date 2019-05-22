import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query = 'Vilnius,Lithuania'
    unit = "metric"
    api_key = '67df05bf49a50660e115606f8eede5bb'
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)

    data = requests.get(url=url).json()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
