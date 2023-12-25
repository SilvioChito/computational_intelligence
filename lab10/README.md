# Reinforcement Learning implementation of the Tic-Tac-Toe game

## Overview

This project implements the game of Tic Tac Toe using Q Reinforcement Learning. The agent learns to make optimal moves by updating Q-values based on rewards obtained during gameplay. Unlike traditional methods, this implementation employs a fixed probability for choosing actions at each state by exploiting the epsilon-greedy strategy. Additionally, rewards are calculated by considering the consequences of letting the opponent have an advantage over a certain actions.

## Q Table


## Reward strategy
For each action, the algorithm can obtain different kind of rewards at the same time (based on different scenarios due to the action taken), which are then summed up.
I've used the following rewards regarding the training phase:
    +1 : the action filled a row or a colum with 2 X's or O's
    +2 : the action blocks an opponent possible winning state
    +5 : the action creates 2 possible way of winning (the opponent will loose at the next move)
    -1 : the action allows the opponent to create a row or a colum with 2 X's or O's
    -5 : allows the opponent to create 2 possible way of winning
    +0.5 : if none of the above

*by action i mean choosing a certain cell 

## Results
