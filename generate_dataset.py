import pandas as pd
import numpy as np
import random

rows = 5000

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
festivals = ["None","Diwali","Eid","Ganesh Chaturthi","Christmas"]
weather = ["Clear","Rainy","Cloudy"]

data = []

for i in range(rows):

    day = random.choice(days)
    hour = random.randint(0,23)
    festival = random.choice(festivals)
    rain = random.randint(0,1)
    weather_cond = random.choice(weather)
    vehicle_count = random.randint(100,2000)

    congestion = vehicle_count / 2000

    if festival != "None":
        congestion += 0.2

    if rain == 1:
        congestion += 0.1

    congestion = min(congestion,1)

    data.append([
        day,
        hour,
        festival,
        rain,
        weather_cond,
        vehicle_count,
        congestion
    ])

columns = [
    "day",
    "hour",
    "festival",
    "rain",
    "weather",
    "vehicle_count",
    "traffic_density"
]

df = pd.DataFrame(data,columns=columns)

df.to_csv("data/traffic_data.csv",index=False)

print("Dataset created successfully with 5000 rows")