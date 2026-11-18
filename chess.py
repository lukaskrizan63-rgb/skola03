from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.

        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.

        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position

        if self.color == "white":
            move = (row + 1, col)
        else:
            move = (row - 1, col)

        if self.is_position_on_board(move):
            return [move]

        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for direction in directions:
            for i in range(1, 8):
                move = (row + direction[0] * i, col + direction[1] * i)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            for i in range(1, 8):
                move = (row + direction[0] * i, col + direction[1] * i)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for direction in directions:
            for i in range(1, 8):
                move = (row + direction[0] * i, col + direction[1] * i)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for direction in directions:
            move = (row + direction[0], col + direction[1])

            if self.is_position_on_board(move):
                moves.append(move)

        return moves


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())
    