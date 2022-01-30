import pandas as pd
import numpy as np

weather_df = pd.read_csv(r'C:\Users\zubae\Downloads\weatherstats_stjohns_daily.csv', parse_dates=['date'], index_col=['date']).sort_index()
print(weather_df)


