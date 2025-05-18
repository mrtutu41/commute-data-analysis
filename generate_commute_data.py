import pandas as pd
import random
from datetime import datetime, timedelta

stations = [
    "Times Sq-42nd", "Grand Central", "Atlantic Av", "Borough Hall",
    "34th-Penn", "14th Union Sq", "Jamaica Ctr", "23rd St",
    "Fulton St", "Brooklyn Br", "125th St", "Wall St"
]

payment_methods = ["MetroCard", "OMNY"]
time_of_day_options = ["Morning", "Afternoon", "Evening", "Night"]


def generate_data(n=100):
    data = []
    base_date = datetime(2024, 5, 1)

    for i in range(n):
        date = base_date + timedelta(days=i % 7)
        entry = random.choice(stations)
        exit = random.choice([s for s in stations if s != entry])
        commute_time = random.randint(8, 45)

        # Slightly vary fare between 2.65 and 2.85
        fare = round(random.uniform(2.65, 2.85), 2)

        payment = random.choice(payment_methods)
        delay = random.choice([0, 0, 0, 2, 3, 5, 8, 10])
        transfer_count = random.randint(0, 2)
        time_of_day = random.choice(time_of_day_options)

        data.append({
            "commuter_id": 1000 + i,
            "date": date.strftime("%Y-%m-%d"),
            "entry_station": entry,
            "exit_station": exit,
            "commute_time_min": commute_time,
            "fare_paid": fare,
            "payment_method": payment,
            "train_delay_min": delay,
            "transfer_count": transfer_count,
            "time_of_day": time_of_day
        })

    return pd.DataFrame(data)


# Generate and export data
df = generate_data(200)
df.to_csv("commute_data.csv", index=False)
