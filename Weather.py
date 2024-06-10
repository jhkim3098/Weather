from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "YOUR_API_KEY"  # OpenWeatherMap API 키를 입력하세요.
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
        if weather:
            return render_template("index.html", weather=weather, city=city)
        else:
            return render_template("index.html", error="City not found")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
