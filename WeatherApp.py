import requests

def get_weather(city):
    """
    Get weather data for a specific city from OpenWeatherMap API.
    
    Args:
        city (str): Name of the City.
        
    Returns: 
        dict: Weather data in JSON format.
    """
    # API endpoint and API key
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "f57f813b0a554437c3c510ea2e729261"

    # parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" #use metric units for temperature (Celsius)
    }

    # send GET request to the API
    response = requests.get(api_endpoint, params=params)

    # check if response was successful
    if response.status_code == 200:
        #return weather data in JSON format
        return response.json()
    else:
        # display error message if request was unsuccessful
        print("Error:", response.text)
        return None

# main program loop
while True:
    # get user input for the city
    city = input("Enter city name (or  'exit' to quit): ")

    if city.lower() == "exit":
        print("Exiting...")
        break

    # fetch weather data for the specified city
    weather_data = get_weather(city)

    if weather_data:
        # extract relevant info from the weather data
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]

        # display weather info
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
    else:
        print("Failed to fetch weather data. Please try again.")