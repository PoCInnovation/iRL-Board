#!/usr/bin/env python3

class Piece:
    def __init__(self, name: str, team: str, **kwargs) -> None:
        """Class for each pieces (**kwargs are here for getting the starting positions)"""

        self.name = name
        self.team = team
        self.pos = [kwargs.get('y'), kwargs.get('x')]
        self.is_start = 1
        self.status = 1
        self.nb_pieces = 32

class Chess:

    def __init__(self, pattern_dict: dict) -> None:
        """
            - type_pieces_order: Order of pieces in a line
            - init_piece_list_index: All the first position for all pieces for respectively the white and the black
            (Info of the type of pieces is also given)
        """
        self.board = []

        self.teams = {"black": [], "white": []}

        self.pattern_dict = pattern_dict
        self.type_pieces_order = ["T", "C", "B", "Q", "K", "B", "C", "T"]
        self.init_piece_list_index = [
            [(j, i, self.type_pieces_order[i] if j == 0 else "P") for j in range(2) for i in range(8)],
            [(j, i, self.type_pieces_order[i] if j == 7 else "P") for j in range(6, 8) for i in range(8)]
        ]

        self.init_board()

    def init_board(self):
        for i in range(8):
            self.board.append([])
            self.board[i] = [None for i in range(8)]
        
        team_name = "black"
        for team in self.init_piece_list_index:
            for i, j, piece in team:
                self.board[i][j] = Piece(name=piece, team=team_name, y=i, x=j)
                self.teams[team_name].append(self.board[i][j])
            team_name = "white"

    def display_board(self) -> None:
        print("[")
        for line in self.board:
            for piece in line:
                if piece != None and piece.team == "black":
                    print("   ", piece.name.lower(), ",\t", sep="", end="")
                elif piece != None:
                    print("   ", piece.name, ",\t", sep="", end="")
                else:
                    print("   ", None, ",", sep="", end="")
            print()
        print("]")

    def get_pattern_piece(self, y: int, x: int):
        return self.pattern_dict[self.board[y][x].name](self, self.board[y][x])
