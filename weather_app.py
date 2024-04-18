import requests
import json

API_KEY = "f8eb7497d3edc31ed6a0d2eb8fb30de6"

def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
    #convertFromKelvinToCelsius
        temperature = main_data['temp'] - 273.15
        humidity = main_data['humidity']
        weather_description = weather_data['weather'][0]['description']

        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description.capitalize()}")


    else:
        print("City not found. Please try again.")
        
        
def main():
    city = input("Enter the name of your city: ")
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)
    
if __name__ == "__main__":
    main()

