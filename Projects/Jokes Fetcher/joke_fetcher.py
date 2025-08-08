# 📌 Project: Random Joke Fetcher
# We’ll call a public API that returns jokes in JSON format, then display them in the terminal.
# url = "https://official-joke-api.appspot.com/random_joke"

import requests

def get_random_joke():
    
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        # raise a request to get a data from the URL
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Raise error for HTTP codes 4xx/5xx
        
        joke_data = response.json()
        
        joke = joke_data['setup']
        punchline = joke_data['punchline']
        return f"{joke} - {punchline}"
    
    except requests.exceptions.Timeout:
        return "Request timeout. Please try again"
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
        