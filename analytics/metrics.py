import pandas as pd

df = pd.read_csv("data/silver_hotel_bookings.csv")

cancellation_rate = df["is_canceled"].mean() * 100
print(f"Cancellation Rate: {cancellation_rate:.2f}%")

avg_price_month = df.groupby("arrival_date_month")["adr"].mean()
print(avg_price_month)

bookings_country = df["country"].value_counts().head(10)
print(bookings_country)

hotel_distribution = df["hotel"].value_counts()
print(hotel_distribution)

avg_stay = df["total_nights"].mean()
print(f"Average Stay Nights: {avg_stay:.2f}")

avg_price_month.to_csv("data/gold_avg_price_per_month.csv")
bookings_country.to_csv("data/gold_bookings_per_country.csv")
hotel_distribution.to_csv("data/gold_hotel_distribution.csv")
