import logging
from etl.extract import get_users, get_posts
from etl.transform import transform_users, transform_posts
from etl.load import load_users, load_posts

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    users_df = get_users()
    posts_df = get_posts()

    users_df = transform_users(users_df)
    posts_df = transform_posts(posts_df)

    load_users(users_df)
    load_posts(posts_df)

if __name__ == "__main__":
    main()