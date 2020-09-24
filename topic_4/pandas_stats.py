"""
Program: pandas_stats.py
Author: Daniel Meeker
Date: 9/24/2020

This program demonstrates statistical data manipulation using
pandas in Python.
"""
import pandas as pd

if __name__ == '__main__':
    game_data = pd.read_csv('ign.csv')
    # print the shape of the dataframe
    print(game_data.shape)
    # remove the 'unnamed' column
    game_data = game_data.drop(game_data.columns[0], axis=1)
    # print the title, genre, and release years by using .loc
    print(game_data.loc[:, ['title', 'genre', 'release_year']])
    # print mean, max, and standard deviation of the scores
    average_score = game_data['score'].mean()
    print("Average Score of games: " + str(average_score))
    print("Highest Score of games: " + str(game_data['score'].max()))
    print("Standard Deviation of scores : " + str(game_data['score'].std()))
    # convert scores column to 100 by multiplying by 10
    game_data['score'] = game_data['score']*10
    # create a new dataframe including only rows with a score above average
    good_game_bool = game_data['score'] > game_data['score'].mean()
    good_game_data = game_data[good_game_bool]
    # print a series that lists the count of scores by platform from the good game data
    print("\nNumber of games with good scores by platform:")
    print(good_game_data['platform'].value_counts())
