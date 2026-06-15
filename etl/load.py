import logging
import sqlite3

logger = logging.getLogger(__name__)

DB_PATH = "db/app.db"

def load_dataframe(df, table_name):
    conn = sqlite3.connect(DB_PATH)

    logger.info("Cargando tabla %s (%d registros) en SQLite", table_name, len(df))

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()