#!/usr/bin/env python3

import serial
from ChessClass import *
from manage_move import *

# A REVERIFIER CAR JE NE PEUX PAS TESTER !!!

def get_arduino_input() -> str:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.reset_input_buffer()
    
    while True:
        if ser.in_waiting > 0:
            str_board = ser.readlines().decode('ascii').rstrip()
            break
    return str_board


def delete_piece(list_board: list, ChessGame: Chess) -> None:
    for index, element in enumerate(list_board):
        y = index / 8
        x = index % 8
        if int(element) == 1 and ChessGame.board[y][x] == None:
            ChessGame.board[y][x] = None
            break
        elif int(element) == 0 and ChessGame.board[y][x] != None:
            ChessGame.board[y][x] = None
            break


def move_piece(list_board: list, ChessClass: Chess) -> None:
    start_coord = []
    dest_coord = []
    for index, element in enumerate(list_board):
        y = index / 8
        x = index % 8
        if int(element) == 1 and ChessGame.board[y][x] == None:
            dest_coord.append(y)
            dest_coord.append(x)
        elif int(element) == 0 and ChessGame.board[y][x] != None:
            start_coord.append(y)
            start_coord.append(x)
    if len(start_coord) != 0 and len(dest_coord) != 0:
        execute_move(start_coord, dest_coord, ChessClass)


def player_move(curr_team: str, ChessGame: Chess):
    """
        In list_board there should be a list of '0' and '1'
    """
    str_board = get_arduino_input()
    list_board = str_board.split(" ")
    is_attack = False if list_board.count('1') != ChessGame.nb_pieces else True

    if is_attack:
        delete_piece(list_board=list_board, ChessGame=ChessGame)
    else:
        move_piece(list_board=list_board, ChessGame=ChessGame)