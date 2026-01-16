
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

try:
    file = input("Enter CSV file name: ")
    df = pd.read_csv(file)
    print("\nDataset Loaded Successfully!")
    print(df.head())
except Exception as e:
    print("Error loading file:", e)
    sys.exit()

if "Date" not in df.columns:
    print("Error: 'Date' column not found in CSV file")
    sys.exit()

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

df.fillna(method="ffill", inplace=True)

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

plt.figure(figsize=(12, 6))
plt.plot(df.index, df["PM2.5"], label="PM2.5", color="red")
plt.plot(df.index, df["PM10"], label="PM10", color="blue")
plt.title("PM2.5 and PM10 Levels Over Time")
plt.xlabel("Date")
plt.ylabel("Concentration (µg/m³)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# 5. CO Trend Visualization
# -------------------------------
plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y=df["CO"], marker="o")
plt.title("Carbon Monoxide (CO) Levels Over Time")
plt.xlabel("Date")
plt.ylabel("CO (mg/m³)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Temperature",
    y="NO2",
    hue="Humidity",
    size="PM2.5"
)
plt.title("Temperature vs NO2 Levels")
plt.xlabel("Temperature (°C)")
plt.ylabel("NO2 (µg/m³)")
plt.show()

rolling_df = df[["PM2.5", "PM10", "NO2"]].rolling(window=3).mean()

rolling_df.plot(figsize=(12, 6))
plt.title("Rolling Average of Pollutants")
plt.xlabel("Date")
plt.ylabel("Concentration")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Between Air Quality & Weather Variables")
plt.show()

df["AQI_Score"] = (
    df["PM2.5"] * 0.4 +
    df["PM10"] * 0.3 +
    df["NO2"] * 0.2 +
    df["CO"] * 0.1
)

plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y=df["AQI_Score"], color="purple")
plt.title("Estimated Air Quality Index (AQI)")
plt.xlabel("Date")
plt.ylabel("AQI Score")
plt.grid(True)
plt.show()

df.to_csv("air_quality_with_aqi.csv")
print("\nAQI Calculation Completed")
print(df[["AQI_Score"]].head())
print("\nResults saved as: air_quality_with_aqi.csv")

