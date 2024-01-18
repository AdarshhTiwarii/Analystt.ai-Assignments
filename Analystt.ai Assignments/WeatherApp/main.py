import requests

def get_weather(city):
    api_key = "30d4741c779ba94c470ca1f63045390a"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
    else:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather in {city}: {weather_description}, Temperature: {temperature}°C")

# Example usage:
city = input("Enter city name: ")
get_weather(city)
