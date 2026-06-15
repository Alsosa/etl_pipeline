import json
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def get_users():
    url = "https://jsonplaceholder.org/users"
    logger.info("Extrayendo datos desde %s", url)

    with open("data/users.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    users_df = pd.DataFrame(data)
    logger.info("Se obtuvieron %d registros", len(users_df))
    return users_df

def get_posts():
    url = "https://jsonplaceholder.org/posts"
    logger.info("Extrayendo datos desde %s", url)

    with open("data/posts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    posts_df = pd.DataFrame(data)
    logger.info("Se obtuvieron %d registros", len(posts_df))
    return posts_df