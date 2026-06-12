from etl import get_data, transform_data, load_csv

def main():
    df = get_data()
    df = transform_data(df)
    load_csv(df)

if __name__ == "__main__":
    main()