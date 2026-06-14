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

def transform_data(df):

    # Simulo datos sucios
    df.loc[0, "email"] = None
    df.loc[1, "email"] = df.loc[2, "email"]  # Duplico un email

    def get_city(address):
        return address["city"]

    def get_company_name(company):
        return company["name"]

    df["city"] = df["address"].apply(get_city)
    df["company_name"] = df["company"].apply(get_company_name)

    # Validaciones
    nulos = df["email"].isnull().sum()
    duplicados = df.duplicated(subset=["email"]).sum()
    logger.info("Emails nulos: %d", nulos)
    logger.info("Duplicados: %d", duplicados)

    # Limpieza
    df = df.drop_duplicates(subset=["email"], keep="first")
    df = df.dropna(subset=["email"])

    # Elimino columnas innecesarias
    df = df.drop(columns=["address", "company"])

    logger.info("Transformación completada. %d registros finales", len(df))
    return df

def load_csv(df, filename="employees_df.csv"):
    df.to_csv(filename, index=False)
    logger.info("Datos guardados en %s", filename)