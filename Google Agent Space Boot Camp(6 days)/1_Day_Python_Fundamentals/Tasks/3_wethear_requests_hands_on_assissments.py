import requests, json

# Fetch live weather data for Hyderabad, India
try: 
    # 17.4065° N, 78.4772° E - Coordinates for Hyderabad, India
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=17.4065&longitude=78.4772&current_weather=true")
    data = response.json()
    print("Live Hyderabad Temperature:", data["current_weather"]["temperature"], "°C")
except requests.RequestException as e:
    print("Error fetching weather data:", e)
    
# Function to get weather for any city using wttr.in API
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    # print(json.dumps(data, indent=4))  # Debug: Print the full JSON response
    # print(data)  # Debug: Print the full JSON response
    
    current = data["current_condition"][0]
    temp = current["temp_C"]
    return f"The temperature in {city} is {temp}°C"

input_city = input("Enter city name to get current temperature: ")
print(get_weather(input_city))
