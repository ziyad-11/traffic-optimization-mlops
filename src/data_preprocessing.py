import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess():

    df = pd.read_csv("data/traffic_data.csv")

    # Encode categorical columns
    le_day = LabelEncoder()
    le_festival = LabelEncoder()
    le_weather = LabelEncoder()

    df["day"] = le_day.fit_transform(df["day"])
    df["festival"] = le_festival.fit_transform(df["festival"])
    df["weather"] = le_weather.fit_transform(df["weather"])

    X = df.drop("traffic_density",axis=1)
    y = df["traffic_density"]

    return X,y