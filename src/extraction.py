import os
import requests
from dotenv import load_dotenv
import json


def get_api_key():
    load_dotenv()
    return os.getenv("TMDB_API_KEY")

def get_response_from_tmdb():
    API_KEY = get_api_key()

    BASE_URL = "https://api.themoviedb.org/3"
    endpoint = "/discover/movie"
    url = f"{BASE_URL}{endpoint}"

    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": 1
    }

    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Success! We are in the matrix.")
        data = response.json()
        with open("data/processed/Movies_Api_Respond.json" , "w") as f :
            json.dump(data, f, indent=4)
    else:
        print("Uh oh, something went wrong.")
        print("Error:", response.text)


get_response_from_tmdb()
