import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# reads the csv
df = pd.read_csv('filtered_data.csv')

# draws up a correlation heat map between power and some variables of the dataset
def corr_heat_map():
    corr_map = df[["power", "energy", "voltage","current","ESP32_temp","WORKSTATION_CPU","WORKSTATION_GPU","WORKSTATION_RAM"]].corr()
    sns.heatmap(corr_map, annot=True, cmap="coolwarm")
    plt.title("Feature correlation with Power usage")
    plt.show()

# shows the total energy used for a given day in kWh (making this the target variable now, realised its better suited)
def daily_energy_usage(df):
    df['server_date'] = pd.to_datetime(df['server_date'])
    df['date'] = df['server_date'].dt.date
    df = df.sort_values('server_date')

    # Get the last energy reading each day
    daily_totals = df.groupby('date')['energy'].last()

    # Find the daily consumption by differencing
    daily_consumed = daily_totals.diff()

    # Plot
    plt.figure(figsize=(12, 5))
    daily_consumed.plot()
    plt.title("Daily Energy Consumption (kWh)")
    plt.xlabel("Date")
    plt.ylabel("Energy Used (kWh)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


corr_heat_map()
daily_energy_usage(df)
