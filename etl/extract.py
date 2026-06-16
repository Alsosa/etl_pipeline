import json
import logging
import os
import pandas as pd
import requests

logger = logging.getLogger(__name__)

API_BASE_URL = "http://127.0.0.1:8000"
USE_API = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "api", "data")

def get_users():
    logger.info("Extrayendo users...")

    if USE_API:
        try:
            response = requests.get(f"{API_BASE_URL}/users")
            response.raise_for_status()
            data = response.json()
            logger.info("Datos obtenidos desde la API")
        except requests.exceptions.RequestException as e:
            logger.warning(
                "Fallo API users, usando JSON local: %s",
                type(e).__name__
            )
            with open(os.path.join(DATA_PATH, "users.json"), "r", encoding="utf-8") as f:
                data = json.load(f)
    else:
        with open("data/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    users_df = pd.DataFrame(data)
    logger.info("Se obtuvieron %d users", len(users_df))

    return users_df

def get_posts():
    logger.info("Extrayendo posts...")

    if USE_API:
        try:
            response = requests.get(f"{API_BASE_URL}/posts")
            response.raise_for_status()
            data = response.json()
            logger.info("Datos obtenidos desde la API")
        except Exception as e:
            logger.warning(
                "Fallo API posts, usando JSON local: %s",
                type(e).__name__
            )
            with open(os.path.join(DATA_PATH, "posts.json"), "r", encoding="utf-8") as f:
                data = json.load(f)
    else:
        with open("data/posts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    
    posts_df = pd.DataFrame(data)
    logger.info("Se obtuvieron %d posts", len(posts_df))

    return posts_df