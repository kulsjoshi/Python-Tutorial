import requests
import argparse
from config import WEATHER_URL
from config import API_KEY

# This function will get a current weather data of the city
def get_weather(city, units):
    param = {
        "q": city,
        "appid": API_KEY,
        "units":units
    }
    
    try:    
        # get the API response from the request
        response = requests.get(url=WEATHER_URL, params=param, timeout=5)
        
        # get data from the json response
        data = response.json()
        
        #find a status cdoe
        status_code = data['cod']
        
        # check if status code is OK and 200
        if(status_code == 200):
            
            # get city name
            name = data['name']
            
            # get current temperature
            temp = data['main']['temp']
            
            # get weather description
            desc = data['weather'][0]['description']
            
            # find a unit symbol based on the user input
            unit_symbol = "°C" if units == "metric" else "°F"
            
            # create complete info of the weather
            complete_info = f"Weather in {name} is {temp} {unit_symbol}, {desc}"
            
            # return 
            return complete_info
        
        # if status code is 404 then show message, city not found
        elif(status_code == "404"):
            return f"City {city} not found"
        
        # if status code is not 200 and 404 then show message, something went wrong
        else:
            return "Something went wrong...!!" 
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"City {city} not found"
        else:
            return f"HTTP error occurred: {e}"
        
    except requests.exceptions.RequestException as e:
        return f"Network error occurred: {e}"