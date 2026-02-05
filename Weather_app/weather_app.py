import requests

API_KEY = "c36c333fcec8024224329fd55d21239e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter your city name: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")
else:
    print("City not found. Try again!")
