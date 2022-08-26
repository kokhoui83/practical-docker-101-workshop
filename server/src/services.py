import requests
import json

def get_random_quote():
    try:
        response = requests.get("http://localhost:8002/quote")

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('server error', response)
    except Exception as e:
        print("failed to get random qoute", e)
        pass