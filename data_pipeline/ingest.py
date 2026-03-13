import pandas as pd

df = pd.read_csv("data/hotel_bookings.csv")

df.to_csv("data/bronze_hotel_bookings.csv", index=False)

print("Bronze layer created")
