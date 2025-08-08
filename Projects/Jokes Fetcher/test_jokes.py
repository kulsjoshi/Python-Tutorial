import unittest
import main
import joke_fetcher

from unittest.mock import patch
from joke_fetcher import requests
from joke_fetcher import get_random_joke

class TestRandomJokeFetcherApi(unittest.TestCase):
    
    def test_get_random_joke_real(self):
        joke = get_random_joke()
        self.assertIsInstance(joke,str)
        self.assertGreater(len(joke),0)
        self.assertNotIn("error",joke.lower())
        self.assertNotIn("timeout",joke.lower())
    
    # 1. What is self?
    # self is the instance of the test class (TestJokerFetcher) itself.
    # In Python, methods defined inside a class always take self as the first parameter to access instance variables and methods.
    # Even though you don’t call the method directly, unittest calls it on an instance of the class and passes self automatically.
    #
    # 2. What is mock_get?
    # mock_get is the mock object that replaces requests.get inside the test method.
    # The @patch("joker.requests.get") decorator injects this mock as a parameter to your test function.
    # This allows you to simulate (mock) how requests.get behaves without making an actual network call.
    # You can set what the mock returns or raise exceptions, so you control how your tested function behaves.

    @patch("joke_fetcher.requests.get")    
    def test_get_joke_sucess(self,mock_get):
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "setup": "Why don't scientists trust atoms?",
            "punchline": "Because they make up everything!"
        }
        result = joke_fetcher.get_random_joke()
        self.assertIn("Why don't scientists trust atoms?", result)
        self.assertIn("Because they make up everything!",result)
        
    @patch("joke_fetcher.requests.get")
    def test_get_joke_failure(self,mock_get):
        
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = Exception("API Error")
        
        with self.assertRaises(Exception):
            joke_fetcher.get_random_joke()
        
    
if __name__ == "__main__":
    unittest.main()