from etl import get_users, get_posts, transform_users, transform_posts, load_users, load_posts

def main():
    users_df = get_users()
    posts_df = get_posts()

    users_df = transform_users(users_df)
    posts_df = transform_posts(posts_df)

    load_users(users_df)
    load_posts(posts_df)

if __name__ == "__main__":
    main()