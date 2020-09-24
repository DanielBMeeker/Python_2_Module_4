"""
Program: pandas_df_assignment.py
Author: Daniel Meeker
Date: 9/24/2020

This program demonstrates creating and merging dataframes
using pandas and also some operations you can perform.
"""
import pandas as pd

if __name__ == '__main__':
    temps = {"Day of Week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
             "Max Temp": [47, 44, 33, 34, 30, 29, 45],
             "Min Temp": [36, 30, 27, 30, 16, 12, 24]
             }
    df_temps = pd.DataFrame(temps, columns=["Day of Week", "Max Temp", "Min Temp"])
    # print statistical data about first frame
    print(df_temps.describe())
    precip = {"Day of Week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
              "Precip": [.21, .01, 0, .01, .001, 0, 0],
              "New Snow": [0, 0, 0, 0.1, 0.3, 0, 0]
              }
    df_precip = pd.DataFrame(precip, columns=["Day of Week", 'Precip', "New Snow"])
    # merge the two dataframes on the day of the week column
    df_merged = pd.merge(df_temps, df_precip, how='left', on='Day of Week')
    print(df_merged)
    # Set the index of the dataframe to 'Day of Week' column
    df_merged.set_index('Day of Week')
    print(df_merged)
    # Convert the Max Temp and Min Temp from Fahrenheit to Celsius
    df_merged['Max Temp'] = (df_merged["Max Temp"]-32)*5/9
    df_merged['Min Temp'] = (df_merged["Min Temp"]-32)*5/9
    # Reindex dataframe so that 'Ave Temp' is right after 'Min Temp'
    df_merged["Ave Temp"] = (df_merged['Max Temp'] + df_merged['Min Temp'])/2
    df_organized = df_merged.reindex(columns=["Day of Week", "Max Temp", "Min Temp", "Ave Temp", "Precip", "New Snow"])
    print(df_organized)
