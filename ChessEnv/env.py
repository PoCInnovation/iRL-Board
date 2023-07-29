#!/usr/bin/env python3

from ChessClass import *
from patterns import *
from input_player import *
from manage_move import *

def ai_move(curr_team: str, ChessGame: Chess) -> int:
    """ This is where we get and execute ai's move """
    move = input("What is your next move ?\n(Format as <piece_name> <y> <x> <y_dest> <x_dest>\n>")
    interpreted_move = interpret_move(move, ChessGame, curr_team)
    if interpreted_move == -1 or check_move(*interpreted_move, ChessGame) == 0:
        return -1
    execute_move(interpreted_move[0], interpreted_move[1], ChessGame)
    # print(f"{interpreted_move}") # Print for the arduino
    return 0


def env() -> None:
    ChessGame = Chess(pattern_dict)
    player = "white"
    ai = "black"
    curr_team = "white"
    while (True):
        ChessGame.display_board()
        print(f"{curr_team} team !")
        if ai == curr_team:
            if ai_move(curr_team=curr_team, ChessGame=ChessGame) == -1:
                continue
        elif player == curr_team:
            # TEMPORARY
            if ai_move(curr_team=curr_team, ChessGame=ChessGame) == -1:
                continue
            # player_move(curr_team=curr_team, ChessGame=ChessGame)
        curr_team = "black" if curr_team == "white" else "white" 

if __name__ == '__main__':
    env()
