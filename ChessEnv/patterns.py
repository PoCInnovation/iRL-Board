#!/usr/bin/env python3

### WARNING: All these functions returns list of tuples organized with 3 values:
###   - 0/1: Nothing or Attack Possibility.
###   - coord y of the destination
###   - coord x of the destination
### Thank you :)

from ChessClass import *


def is_destination_valid(y: int, x: int):
    """ Check with some coord (x, y) if destination is valid """
    if (y >= 0 and y < 8) and (x >= 0 and x < 8):
        return 1
    else:
        return 0


def pawn_pattern(chess: Chess, piece: Piece) -> list:
    """ Pattern for all pawns """
    moves = []
    if piece.team == "black":
        add_y = 1
    else:
        add_y = -1
    y_dest = piece.pos[0] + add_y
    if is_destination_valid(y=y_dest, x=piece.pos[1]) and chess.board[y_dest][piece.pos[1]] == None:
        moves.append((0, y_dest, piece.pos[1]))
    if piece.is_start and is_destination_valid(y=y_dest + add_y, x=piece.pos[1]) and chess.board[y_dest + add_y][piece.pos[1]] == None:
        moves.append((0, y_dest + add_y, piece.pos[1]))
    for i in list([1, -1]):
        if is_destination_valid(y=y_dest, x=piece.pos[1] + i) and chess.board[y_dest + add_y][piece.pos[1] + i] != None:
            if chess.board[y_dest + add_y][piece.pos[1] + i].team != piece.team:
                moves.append((1, y_dest, piece.pos[1] + i))
    return moves


def check_one_side(
    curr_x: int,
    curr_y: int,
    add_x: int,
    add_y: int,
    chess: Chess,
    moves: list,
    team: str
) -> None:
    """ Check moves in one direction """
    while is_destination_valid(curr_y, curr_x):
        if chess.board[curr_y][curr_x] == None:
            moves.append((0, curr_y, curr_x))
        elif chess.board[curr_y][curr_x].team != team:
            moves.append((1, curr_y, curr_x))
            break
        else:
            break
        curr_x += add_x
        curr_y += add_y


def check_knight_sides(
    curr_x: int,
    curr_y: int,
    add_x_list: list,
    add_y_list: list,
    chess: Chess,
    moves: list,
    team: str
) -> None:
    """ Check moves in one direction for the knight only """
    for add_y in add_y_list:
        for add_x in add_x_list:
            is_valid = is_destination_valid(curr_y + add_y, curr_x + add_x)
            if is_valid:
                if chess.board[curr_y + add_y][curr_x + add_x] == None:
                    moves.append((0, curr_y + add_y, curr_x + add_x))
                elif chess.board[curr_y + add_y][curr_x + add_x].team != team:
                    moves.append((1, curr_y + add_y, curr_x + add_x))


def tower_pattern(chess: Chess, piece: Piece) -> list:
    """ Pattern for all towers """
    moves = []
    for i in list([1, -1]):
        check_one_side(piece.pos[1], piece.pos[0] + i, 0, i, chess, moves, piece.team)
    for i in list([1, -1]):
        check_one_side(piece.pos[1] + i, piece.pos[0], i, 0, chess, moves, piece.team)        
    return moves


def bishop_pattern(chess: Chess, piece: Piece) -> list:
    """ Pattern for all bishops """
    moves = []
    directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    for add_y, add_x in directions:
        check_one_side(piece.pos[1] + add_x, piece.pos[0] + add_y, add_x, add_y, chess, moves, piece.team)
    return moves


def knight_pattern(chess: Chess, piece: Piece) -> list:
    """ Pattern for all Knight  named C (for "cavalier" in french) in the game"""
    moves = []
    check_knight_sides(piece.pos[1], piece.pos[0], [-1, 1], [-2, 2], chess, moves, piece.team)
    check_knight_sides(piece.pos[1], piece.pos[0], [-2, 2], [-1, 1], chess, moves, piece.team)
    return moves


def queen_pattern(chess: Chess, piece: Piece) -> list:
    """ Pattern for all queens """
    return tower_pattern(chess, piece) + bishop_pattern(chess, piece)


def king_pattern(chess: Chess, piece: Piece):
    """ Pattern for all Kings """
    moves = []
    directions = [(i, j) for j in range(-1, 2) for i in range(-1, 2) if i != 0 or j != 0]
    for add_y, add_x in directions:
        is_valid = is_destination_valid(piece.pos[0] + add_y, piece.pos[1] + add_x)
        if is_valid:
            if chess.board[piece.pos[0] + add_y][piece.pos[1] + add_x] == None:
                moves.append((0, piece.pos[0] + add_y, piece.pos[1] + add_x))
            elif chess.board[piece.pos[0] + add_y][piece.pos[1] + add_x].team != piece.team:
                moves.append((1, piece.pos[0] + add_y, piece.pos[1] + add_x))
    return moves


pattern_dict = dict(
    {
        "T": tower_pattern,
        "B": bishop_pattern,
        "C": knight_pattern,
        "Q": queen_pattern,
        "K": king_pattern,
        "P": pawn_pattern
    }
)
