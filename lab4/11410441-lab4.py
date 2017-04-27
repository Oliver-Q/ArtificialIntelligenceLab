from games import (GameState, Game, TicTacToe, random_player, alphabeta_player, alphabeta_search, alphabeta_full_search)
import time
import random

def random_player(game, state):
    "A player that chooses a legal move at random."
    "A player that chooses a legal move at random."
    return random.choice(game.actions(state))


def alphabeta_player(game, state):
    return alphabeta_full_search(state, game)

def alphabeta_prune_player(game, state):
    return alphabeta_search(state, game, 8)

def human_player(game, state):
    inputed_num = input("Input position in the form of x,y \n")
    my_num = (int(inputed_num[0]), int(inputed_num[2]))
    return my_num

def play_game(game, *players):
    """Play an n-person, move-alternating game."""

    state = game.initial
    while True:
        for player in players:
            move = player(game, state)
            state = game.result(state, move)
            if game.terminal_test(state):
                game.display(state)
                return game.utility(state, game.to_move(game.initial))


result_all = 0
pstart = time.clock()

for i in range(100):
    ttt = TicTacToe()
    play_ttt = play_game(ttt, random_player, alphabeta_player)
    print("The result: %s, %s" %(i, play_ttt))
    result_all += play_ttt

pend = time.clock()
ptime = pend - pstart

print("The winning rate: %s" %(-result_all/100))
print("The winning time: %s" %(ptime))


result_all = 0
pstart = time.clock()

for i in range(100):
    ttt = TicTacToe()
    play_ttt = play_game(ttt, random_player, alphabeta_prune_player)
    print("The result: %s, %s" %(i, play_ttt))
    result_all += play_ttt

pend = time.clock()
ptime = pend - pstart

print("The winning rate: %s" %(-result_all/100))
print("The winning time: %s" %(ptime))

def play_game(game, *players):
    """Play an n-person, move-alternating game."""

    state = game.initial
    while True:
        for player in players:
            move = player(game, state)
            state = game.result(state, move)
            game.display(state)
            print("\n")
            if game.terminal_test(state):
                game.display(state)
                return game.utility(state, game.to_move(game.initial))

ttt.display(ttt.initial)
print("\n")
play_ttt = play_game(ttt, human_player, alphabeta_player)
print("The result: %s" %(play_ttt))

