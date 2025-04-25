import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# reads the csv
df = pd.read_csv('server_data.csv')

# draws up a correlation heat map between power and some variables of the dataset
def corr_heat_map():
    corr_map = df[['power', 'voltage', 'current', 'ESP32_temp', 'WORKSTATION_CPU', 'WORKSTATION_GPU', 'WORKSTATION_RAM']].corr()
    sns.heatmap(corr_map, annot=True, cmap="coolwarm")
    plt.title("Feature correlation with Power usage")
    plt.show()

# draws up a line graph that shows the average power usage of the servers each day
def average_daily_power_graph():
    df['server_date'] = pd.to_datetime(df['server_date'])
    df['date'] = df['server_date'].dt.date
    daily_avg_power = df.groupby('date')['power'].mean()
    plt.figure(figsize=(12, 5))
    daily_avg_power.plot()
    plt.xlabel('Time')
    plt.ylabel('Power (w)')
    plt.title('Average Daily Power Usage')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

corr_heat_map()
average_daily_power_graph()

