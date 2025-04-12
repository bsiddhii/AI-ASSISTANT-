import requests

def weather(city_name):
    api_key = "c81fc38a043fed68408254f905ff9893"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            return temperature, description, humidity
        else:
            print(f"Error: {data['message']} (Code: {data['cod']})")
            return None, None, None  # <-- Add this

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None, None, None  # <-- Add this
    except KeyError as e:
        print(f"Data parsing error: {e}")
        print(f"Full response for debugging: {data}")
        return None, None, None  # <-- Add this
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None  # <-- Add this

# Example usage
temp, desc, hum = weather("bareilly")
if temp is not None:
    print(f"Temp: {temp}°C, Desc: {desc}, Humidity: {hum}%")
