"""
Program: numpy_card_game.py
Author: Daniel Meeker
Date: 9/24/2020

This program demonstrates more numpy applications by creating a card game
"""
import numpy as np

if __name__ == '__main__':
    # create an array of numbers 1-36
    array = np.arange(1, 37)
    # print(array)
    # randomize the order of the array
    np.random.shuffle(array)
    # print(array)
    # reshape to a 6x6 array
    array = array.reshape(6, 6)
    # print(array)
    # create an identity array
    id_array = np.identity(6, dtype=int)
    # print(id_array)
    # create a 6x6 array of all 1's
    ones_array = np.full((6, 6), 1, dtype=int)
    # print(ones_array)
    # subtract the ones array from the identity array
    working_array = id_array - ones_array
    # print(working_array)
    # multiply random array by working array
    negative_array = working_array*array
    # print(working_array)
    # combine the array of random numbers and negative numbers so that the signs are flipped
    finalized_array = array + negative_array * 2
    # print(finalized_array)
    scores_array = finalized_array.sum(1)
    print("The Final scores are as follows:")
    print(scores_array)
    # Find the highest score and the winning player
    highest_score = scores_array.max()
    winner = scores_array.argmax() + 1
    print("The Winning score was: " + str(highest_score))
    print("Player " + str(winner) + " is the winner!")
