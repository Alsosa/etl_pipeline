import logging
from extract import get_users, get_posts
from transform import transform_users, transform_posts
from load import load_dataframe

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    users_df = get_users()
    posts_df = get_posts()

    users_df = transform_users(users_df)
    posts_df = transform_posts(posts_df)

    load_dataframe(users_df, "users")
    load_dataframe(posts_df, "posts")

if __name__ == "__main__":
    main()