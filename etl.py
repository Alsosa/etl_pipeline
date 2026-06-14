import logging
import requests
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    logger.info("Extrayendo datos desde %s", url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error("Error al obtener datos: %s", e)
        raise

    data = response.json()
    users_df = pd.DataFrame(data)
    breakpoint()
    logger.info("Se obtuvieron %d registros", len(users_df))
    return users_df

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    logger.info("Extrayendo datos desde %s", url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error("Error al obtener datos: %s", e)

    data = response.json()
    posts_df = pd.DataFrame(data)
    logger.info("Se obtuvieron %d registros", len(posts_df))
    return posts_df

def transform_users(users_df):

    # Simulo datos sucios
    users_df.loc[0, "email"] = None
    users_df.loc[1, "email"] = users_df.loc[2, "email"]  # Duplico un email

    def get_city(address):
        return address["city"]

    def get_company_name(company):
        return company["name"]

    users_df["city"] = users_df["address"].apply(get_city)
    users_df["company_name"] = users_df["company"].apply(get_company_name)

    # Validaciones
    nulos = users_df["email"].isnull().sum()
    duplicados = users_df.duplicated(subset=["email"]).sum()
    logger.info("Emails nulos: %d", nulos)
    logger.info("Duplicados: %d", duplicados)

    # Limpieza
    users_df = users_df.drop_duplicates(subset=["email"], keep="first")
    users_df = users_df.dropna(subset=["email"])

    # Elimino columnas innecesarias
    users_df = users_df.drop(columns=["address", "company"])

    logger.info("Transformación completada. %d registros finales", len(users_df))
    return users_df

def transform_posts(posts_df):
    posts_df = posts_df.rename(columns={"userId": "user_id"})
    null_titles = posts_df["title"].isnull().sum()
    logger.info("Posts con titulos nulos %d", null_titles)

    posts_df = posts_df.dropna(subset=["title"])

    posts_df = posts_df[["id", "user_id", "title"]]

    logger.info("Transformación de posts completada. Registros: %d", len(posts_df))

    return posts_df

def load_csv(df, filename="employees_df.csv"):
    df.to_csv(filename, index=False)
    logger.info("Datos guardados en %s", filename)