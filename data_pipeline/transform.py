import pandas as pd


def transform_data():

    df = pd.read_csv("data/bronze_hotel_bookings.csv")

    df = df.drop_duplicates()

    df["children"] = df["children"].fillna(0)
    df["country"] = df["country"].fillna("Unknown")
    df["agent"] = df["agent"].fillna(0)

    df = df.drop(columns=["company"])

    df = df[df["adr"] >= 0]

    df = df[df["adr"] < 1000]

    df = df[(df["adults"] + df["children"] + df["babies"]) > 0]

    df = df[~((df["adults"] == 0) & (df["children"] > 0))]

    df = df[(df["stays_in_week_nights"] + df["stays_in_weekend_nights"]) > 0]

    df["total_nights"] = df["stays_in_week_nights"] + df["stays_in_weekend_nights"]

    df["total_guests"] = df["adults"] + df["children"] + df["babies"]

    df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])

    df.to_csv("data/silver_hotel_bookings.csv", index=False)


if __name__ == "__main__":
    transform_data()
