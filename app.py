from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = '2cc360c77a57a3a0411c750966d0e97e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        weather_data = response.json()
        if weather_data['cod'] == 200:
            weather = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            }
            return render_template('index.html', weather=weather)
        else:
            error = weather_data['message']
            return render_template('index.html', error=error)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
