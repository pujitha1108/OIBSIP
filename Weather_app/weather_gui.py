import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "c36c333fcec8024224329fd55d21239e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ✅ Create the window first
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="white")

# ✅ Create the input box BEFORE the function
city_entry = tk.Entry(root, font=("Arial", 14), width=30)
city_entry.pack(pady=10)

# ✅ Now define the function
def get_weather():
    city = city_entry.get().strip()
    print(f"You typed: {city}")  # Debug
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    print(f"URL used: {url}")  # Debug
    response = requests.get(url)
    data = response.json()
    print(data)  # Debug

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        result_label.config(text=f"{city}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nCondition: {condition}")
    else:
        messagebox.showerror("Error", "City not found. Try again!")

# ✅ Button and result label
search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14), bg="lightblue")
search_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="darkgreen")
result_label.pack(pady=10)

root.mainloop()
