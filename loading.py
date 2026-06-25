import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.6895,
    "longitude": 139.6917,
    "hourly": "temperature_2m",
    "forecast_days": 1,
}

response = requests.get(url, params=params)
data = response.json()

times = data["hourly"]["time"]
temperatures = data["hourly"]["temperature_2m"]


df = pd.DataFrame(
    {
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
    }
)
temps = df["temperature"].to_numpy()
time = df["time"].to_numpy()
plt.plot(time, temps, marker="o")

plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Tokyo Temperature Forecast")
plt.tight_layout()

plt.show()
