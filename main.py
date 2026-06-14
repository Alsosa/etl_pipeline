from etl import get_users, get_posts, transform_data, load_csv

def main():
    users_df = get_users()
    posts_df = get_posts()
    final_df = transform_data(df)
    load_csv(final_df)

if __name__ == "__main__":
    main()