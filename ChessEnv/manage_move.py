#!/usr/bin/env python3

from ChessClass import *

# That will surely disappear later
def interpret_move(move: str, ChessGame: Chess, team: str):
    """
        splited infos should have (in list):
            - <y_start> <x_start>
            - <y_dest> <x_dest>
    """
    splited_infos = move.split(" ")
    try:
        coord_start = [int(splited_infos[0]), int(splited_infos[1])]
        coord_destination = [int(splited_infos[2]), int(splited_infos[3])]
    except:
        print("You put a wrong input try again !")
        return -1
    piece = ChessGame.board[coord_start[0]][coord_start[1]]
    if piece == None:
        print("There is no pieces here !")
        return -1
    if piece.team != team:
        print("You can't move pieces from another team !")
        return -1
    return [coord_start, coord_destination]


def check_move(coord_start: list, coord_dest: list, ChessGame: Chess) -> int:
    """ Check if input move is valid """
    all_moves = ChessGame.get_pattern_piece(coord_start[0], coord_start[1])
    for move in all_moves:
        print(move)
        if coord_dest[0] == move[1] and coord_dest[1] == move[2]:
            print("Good !")
            return 1
    print("Bad move !")
    return 0


def execute_move(coord_start: list, coord_dest: list, ChessGame: Chess):
    """ Execute move """
    piece = ChessGame.board[coord_start[0]][coord_start[1]]
    piece.pos = coord_dest.copy()
    if piece.is_start == 1:
        piece.is_start = 0
    if ChessGame.board[coord_dest[0]][coord_dest[1]] != None:
        ChessGame.nb_pieces -= 1
    ChessGame.board[coord_dest[0]][coord_dest[1]] = piece
    ChessGame.board[coord_start[0]][coord_start[1]] = None

