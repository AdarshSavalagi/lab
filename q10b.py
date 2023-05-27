import json

def fetch_weather_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract relevant information from the JSON data
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    # Print the weather information
    print("Temperature: {}°C".format(temperature))
    print("Humidity: {}%".format(humidity))
    print("Description: {}".format(description))

# Test the program
json_file = "weather_data.json"  # Replace with the actual JSON file name
fetch_weather_data(json_file)
