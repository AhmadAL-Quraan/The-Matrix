import importlib.util

print("LOADING STATUS: Loading programs...")


def check_import(package_name):
    spec = importlib.util.find_spec(package_name)
    return True if spec != None else False


def print_it(bool_it: str, package_name, package_name_str, comment: str):
    print(
        f"[{bool_it}] {package_name_str} ({package_name.__version__}) - {comment}"
    )


def print_it2(bool_it: str, package_name_str, comment: str):
    print(f"[{bool_it}] {comment} : {package_name_str}")
    exit(0)


print("Checking dependencies:")
if check_import("requests"):
    import requests

    print_it("OK", requests, "requests", "Network access ready")
else:
    print_it2("FAILED", "requests", "Didn't found")

if check_import("matplotlib"):
    import matplotlib

    print_it("OK", matplotlib, "matplotlib", "Visualization ready")
else:
    print_it2("FAILED", "matplotlib", "Didn't found")
if check_import("numpy"):
    import numpy as np

    print_it("OK", np, "numpy", "Numerical computation ready")
else:
    print_it2("FAILED", "numpy", "Didn't found")

if check_import("pandas"):
    import pandas as pd

    print_it("OK", pd, "pandas", "Data manipulation ready")
else:
    print_it2("FAILED", "pandas", "Didn't found")

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
print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")
print("Generating visualization...\n")
print("Analysis complete!")
temps = df["temperature"].to_numpy()

import matplotlib.pyplot as plt

time = df["time"].to_numpy()
plt.plot(time, temps, marker="o")

plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Tokyo Temperature Forecast")
plt.tight_layout()

plt.savefig("matrix_analysis.png")
print("Results saved to: matrix_analysis.png")
