import argparse

from weather import get_weather
from forecast import get_forecast

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
# 
# Benefits of argparse for your scripts
# You can easily add multiple options/flags.
# You get built-in help messages (so users know how to use your script).
# You avoid writing repetitive input validation code.
# It makes your script professional and user-friendly.
def main():
    
     # create a argparse
    parser = argparse.ArgumentParser(description="Get Current weather for a city.")
    
    # create first argument to get the city information from the user
    parser.add_argument("city", help="Name of the city to featch a weather from")
    
    # add optional argument for the unit
    parser.add_argument(
        "--units",
        choices=["metric","imperial"],
        default="metric",
        help="Units of tempreture. 'metric' for Celsius, 'imperial' for Fahrenheit (default: metric)"
    )
    
    # add optional argument for the forecast information
    parser.add_argument(
        "--forecast",
        action="store_true",
        help="Show 5-days of forecast instead of the current weather"
    )
    args = parser.parse_args()
    
    # if user selects forecasgt then we will show forecast information 
    # else we show current weather
    if args.forecast:
        print(get_forecast(args.city, args.units))
    else:
        print(get_weather(args.city, args.units))
        
if __name__=="__main__":
    main()