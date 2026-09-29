import os
import requests
from dotenv import load_dotenv
import json
import time 
import glob
import pandas as pd


def get_api_key():
    load_dotenv()
    return os.getenv("TMDB_API_KEY")

def get_response_from_tmdb():
    API_KEY = get_api_key()

    BASE_URL = "https://api.themoviedb.org/3"
    endpoint = "/discover/movie"
    url = f"{BASE_URL}{endpoint}"
    for current_page in range(1, 151):
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "page": current_page
        }
        try :
            response = requests.get(url, params=params)
            
            print("Status Code:", response.status_code)
    
            if response.status_code == 200:
                print("Success! We are in the matrix.")
                data = response.json()
                with open("data/raw/Movies_Api_Respond_p"+str(current_page)+".json" , "w") as f :
                    json.dump(data, f, indent=4)
            else:
                print("Uh oh, something went wrong.")
                print("Error:", response.text)

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

        time.sleep(0.2)
        


get_response_from_tmdb()

