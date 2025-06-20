import requests
import datetime
import os

# Set your location
import sys
city = sys.argv[1] if len(sys.argv) > 1 else "Lagos"
  # Change this to your actual city

# API Endpoint
url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()

    current = data['current_condition'][0]
    temp_c = current['temp_C']
    weather = current['weatherDesc'][0]['value']
    feels_like = current['FeelsLikeC']
    humidity = current['humidity']

    # Format report
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (
        f"📅 Time: {now}\n"
        f"📍 Location: {city}\n"
        f"🌡️ Temperature: {temp_c}°C (Feels like {feels_like}°C)\n"
        f"💧 Humidity: {humidity}%\n"
        f"🌤️ Condition: {weather}\n"
    )

    print(report)

    # Save to file
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/weather_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(report)

    print(f"✅ Report saved to {filename}")

except Exception as e:
    print(f"❌ Failed to fetch weather data: {e}")
