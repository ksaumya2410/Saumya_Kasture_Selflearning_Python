
import requests

# Function to convert weather codes into descriptions
def get_weather_description(code):
    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    return weather_conditions.get(code, "Unknown weather condition")


# Function to fetch and save weather data
def fetch_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,relative_humidity_2m,"
            "apparent_temperature,precipitation,"
            "weather_code,wind_speed_10m"
        ),
        "timezone": "auto"
    }

    try:
        # Send HTTP GET request
        response = requests.get(
            url,
            params=parameters,
            timeout=10
        )

        # Check HTTP status code
        if response.status_code != 200:
            print("Error: HTTP status code", response.status_code)
            return

        # Parse JSON response
        data = response.json()

        # Extract current weather information
        current = data["current"]
        units = data["current_units"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        feels_like = current["apparent_temperature"]
        precipitation = current["precipitation"]
        weather_code = current["weather_code"]
        wind_speed = current["wind_speed_10m"]
        timezone = data.get("timezone", "Not available")

        description = get_weather_description(weather_code)

        # Format the weather report
        report = f"""
        AUTOMATED WEATHER REPORT
        -----------------------
        Latitude: {latitude}
        Longitude: {longitude}
        Timezone: {timezone}
        Observation Time: {current.get('time', 'Not available')}

        Temperature: {temperature} {units['temperature_2m']}
        Feels Like: {feels_like} {units['apparent_temperature']}
        Humidity: {humidity} {units['relative_humidity_2m']}
        Precipitation: {precipitation} {units['precipitation']}
        Wind Speed: {wind_speed} {units['wind_speed_10m']}
        Weather Condition: {description}
        """

        # Display the report
        print(report)

        # Save report to a text file
        with open("weather_report.txt", "w", encoding="utf-8") as file:
            file.write(report)

        print("Weather report saved to weather_report.txt")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the weather API.")

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    except (ValueError, KeyError, TypeError) as error:
        print("Error processing weather data:", error)


# Main program
try:
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90.")

    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180.")

    fetch_weather(latitude, longitude)

except ValueError as error:
    print("Invalid input:", error)
