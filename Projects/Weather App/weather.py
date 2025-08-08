import requests
import argparse
from config import URL
from config import API_KEY

def get_weather(city):
    param = {
        "q": city,
        "appid": API_KEY,
        "units":"metric"
    }
    
    try:    
        response = requests.get(url=URL, params=param, timeout=5)
    
        data = response.json()
        # print(f"JSON DATA:\n{data}")
        status_code = data['cod']
        
        if(status_code == 200):
            
            name = data['name']
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            
            complete_info = f"Weather in {name} is {temp} Celsius, {desc}"
            return complete_info
        
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
    
 
# Explanation:
# 
# We use argparse.ArgumentParser to define expected command-line arguments.
# city is a positional argument (required).
# args.city contains the value passed on the command line.
# We print the full request URL to help with debugging.
# 
# What is argparse?
# It’s a standard Python library to handle command-line arguments easily.
# Lets users pass inputs or options to your script/program when running it from a terminal.
# Automatically generates help messages (-h or --help).
# Parses and validates inputs, so you don’t have to write manual input checks.    
def main():
    parser = argparse.ArgumentParser(description="Get Current weather for a city.")
    parser.add_argument("city", help="Name of the city to featch a weather from")
    args = parser.parse_args()
    print(get_weather(args.city))
    
if __name__=="__main__":
    main()