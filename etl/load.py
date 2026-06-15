import logging
import sqlite3

logger = logging.getLogger(__name__)

DB_PATH = "data/app.db"

def load_users(users_df):
    conn = sqlite3.connect(DB_PATH)

    logger.info("Cargando users en SQLite")

    users_df.to_sql(
        "users",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()

def load_posts(posts_df):
    conn = sqlite3.connect(DB_PATH)

    logger.info("Cargando posts en SQLite")

    posts_df.to_sql(
        "posts",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()