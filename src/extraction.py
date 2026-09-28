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
