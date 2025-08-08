import requests
import argparse
from config import FORECAST_URL
from config import API_KEY
from datetime import datetime

# This function will get a current weather data of the city
def get_forecast(city, units):
    param = {
        "q": city,
        "appid": API_KEY,
        "units":units
    }
    
    try:    
        response = requests.get(url=FORECAST_URL, params=param, timeout=5)
    
        # parse json response
        data = response.json()
        
        # find status code
        status_code = data['cod']
        print(f"Status CODE: {status_code}")
        
        # if status code is 200
        if(status_code == "200"):
            
            # find unit symbol based on the user selection
            unit_symbol = "°C" if units == "metric" else "°F"
            
            # find city name from the API response
            city_name = data['city']['name']
            
            # create initial forecast string and we will appened more info in the for loop
            forecast_str = f"5-days forecast for {city_name}\n"
            
            # create forecasts object and put API value in it
            forecasts = data['list']
            
            # create empty list
            daily_forecasts = {}

            # run a for loop for each item in the list
            for entry in forecasts:
                # find date and time from the API e.g "2025-08-08 03:00:00"
                dt_txt = entry['dt_txt']
                # split the date and time using .split()
                date,time = dt_txt.split()
                
                # only consider temp when time if 12:00:00 in the afternoon, as the particular day has
                # lot of information and we dont want all the information
                if(time == "12:00:00"):
                    
                    # find temperature
                    temp=entry['main']['temp']
                    
                    # find description of particular day
                    desc = entry['weather'][0]['description']
                    
                    # create a date object
                    date_obj = datetime.strptime(date, "%Y-%m-%d")
                    date_formatted = date_obj.strftime("%a, %b %d")
                    
                    # create list comprehension where temp and desc will be shown with the timestamp
                    daily_forecasts[date_formatted] = (temp,desc)
                
            # run a for loop for appending the string with the data    
            for date, (time, description) in daily_forecasts.items():
                # append the string from the for loop item
                forecast_str += f"{date}: {time}{unit_symbol}, {description}\n"
        
            return forecast_str
        
        elif(status_code == "404"):
            return f"City {city} not found"
        
        else:
            return "Something went wrong...!!" 
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"City {city} not found"
        else:
            return f"HTTP error occurred: {e}"
        
    except requests.exceptions.RequestException as e:
        return f"Network error occurred: {e}"