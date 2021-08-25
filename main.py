import random
from random import seed
from random import shuffle
import numpy as np
import pandas as pd


def get_expectation(rating1, rating2):
    exp1 = (1.0 / (1.0 + pow(10, ((rating2-rating1)/400))))
    exp2 = (1.0 / (1.0 + pow(10, ((rating1-rating2)/400))))
    # if exp1 > exp2:
        # print("Player 1 is expected to win " + str(exp1 * 100) + "% of the time")
    # else:
        # print("Player 2 is expected to win " + str(exp2 * 100) + "% of the time")
    return exp1, exp2


def determine_winner(n1, n2):
    winner = random.randint(1, 2)
    if winner == 1:
        actual1 = 1
        actual2 = 0
        # print("Winner: " + n1)
    else:
        actual1 = 0
        actual2 = 1
        # print("Winner: " + n2)
    return actual1, actual2


def modify_rating(rating, expected, actual, k_value):
    m = (rating + (k_value * (actual - expected)))
    return m


def run_elo(player1, player2, k_value):
    rating1 = player1[1]
    rating2 = player2[1]
    # print("Rating for " + player1[0] + ": " + str(rating1))
    # print("Rating for " + player2[0] + ": " + str(rating2))
    # print("K-value for rating modification: " + str(k_value))
    e1, e2 = get_expectation(rating1, rating2)
    a1, a2 = determine_winner(player1[0], player2[0])
    m1 = modify_rating(rating1, e1, a1, k_value)
    m2 = modify_rating(rating2, e2, a2, k_value)
    # print("Updated Rating for " + player1[0] + ": " + str(m1))
    # print("Updated Rating for " + player2[0] + ": " + str(m2))
    player1[1] = m1
    player2[1] = m2
    return player1, player2


def draw_opponents():
    drawn = random.sample(range(50), 2)
    # print(drawn)
    draw1, draw2 = drawn[0], drawn[1]
    return draw1, draw2


def run_sim(d_list, k_value, n_value):
    for i in range(n_value):
        d1, d2 = draw_opponents()
        p1 = d_list[d1]
        p2 = d_list[d2]
        player1, player2 = run_elo(p1, p2, k_value)
        d_list[d1] = player1
        d_list[d2] = player2
    return d_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    k = 24
    n = 200
    dataset = pd.read_csv('default.csv')
    # print(dataset)
    data_list = [list(row) for row in dataset.values]
    # print(data_list)
    data_list = run_sim(data_list, k, n)
    data_list.sort(key=lambda x: int(x[1]), reverse=True)
    df = pd.DataFrame(data_list, columns=['Name', 'Rating'])
    print(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
