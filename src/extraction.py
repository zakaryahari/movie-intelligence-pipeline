import os
import requests
from dotenv import load_dotenv
import json


def get_api_key():
    load_dotenv()
    return os.getenv("TMDB_API_KEY")
