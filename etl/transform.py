import os
import logging

os.makedirs("data_quality", exist_ok=True)

logger = logging.getLogger(__name__)

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
    invalid_users = users_df[
        users_df["email"].isnull() |
        users_df.duplicated(subset=["email"], keep=False)]

    logger.info("Usuarios invalidos detectados: %d", len(invalid_users))

    invalid_users.to_csv(
        "data_quality/invalid_users.csv",
        index=False
    )

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