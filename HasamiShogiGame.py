# Author: Aaron Trinh
# Date: 11/30/2021
# Description: A program to play the variant 1 version of the Hasami Shogi game.
#              This includes a functioning board and pieces as well as accompanying methods.


class HasamiShogiGame:
    """A class used to play the Hasami Shogi game."""

    def __init__(self):
        """Create an object that represents a Hasami Shogi game."""
        self._active_player = "BLACK"
        self._game_state = "UNFINISHED"
        self._red_captured = 0
        self._black_captured = 0
        self._board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                       ["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
                       ["b", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["c", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["d", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["e", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["f", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["g", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["h", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]

    def get_game_state(self):
        """Returns the game state."""
        return self._game_state

    def set_game_state(self, state):
        """Set the game state to state."""
        self._game_state = state

    def get_active_player(self):
        """Returns the active player."""
        return self._active_player

    def set_active_player(self, player):
        """Set the active player to player."""
        self._active_player = player

    def get_num_captured_pieces(self, player):
        """Returns the number of captured pieces for a player."""
        if player == "RED":
            return self._red_captured
        if player == "BLACK":
            return self._black_captured

    def display_board(self):
        """Display the game board in its current state."""
        for row in self._board:
            print("")
            for square in row:
                print(square, end=" ")
        print("")

    def get_square_occupant(self, square):
        """Returns the occupant of a square."""
        # Convert the square string to board coordinates.
        key = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
        square_row = square[0].upper()
        square_row = key[square_row]
        square_col = int(square[1])

        # Return the occupant of the square.
        occupant = self._board[square_row][square_col]
        if occupant == "B":
            return "BLACK"
        elif occupant == "R":
            return "RED"
        else:
            return "NONE"

    def check_move(self, start_row, start_col, end_row, end_col):
        """Returns True if a move is legal and possible, False otherwise."""
        # Check if we're moving to a spot on the game board
        if end_row > 9 or end_row < 1:
            return False
        if end_col > 9 or end_col < 1:
            return False

        # Check if we're moving vertically or horizontally
        if start_row == end_row:
            direction = "Horizontal"
        elif start_col == end_col:
            direction = "Vertical"
        else:
            return False

        # Check if the move is blocked by another piece.
        if direction == "Horizontal":
            if start_col > end_col:
                for index in range(end_col, start_col):
                    if self._board[start_row][index] != ".":
                        return False
            if end_col > start_col:
                for index in range(start_col+1, end_col):
                    if self._board[start_row][index] != ".":
                        return False
        elif direction == "Vertical":
            if start_row > end_row:
                for index in range(end_row, start_row):
                    if self._board[index][start_col] != ".":
                        return False
            if end_row > start_row:
                for index in range(start_row+1, end_row):
                    if self._board[index][start_col] != ".":
                        return False
        return True

    def make_capture(self, end_row, end_col):
        """Checks a move and performs any captures that would result from it."""
        counter = 0
        if self._active_player == "BLACK":
            ally = "B"
            enemy = "R"
        else:
            ally = "R"
            enemy = "B"

        # Check above
        try:
            if self._board[end_row - 1][end_col] == enemy:
                if self._board[end_row - 2][end_col] == ally:
                    self._board[end_row - 1][end_col] = "."
                    counter += 1
        except IndexError:
            pass

        # Check below
        try:
            if self._board[end_row + 1][end_col] == enemy:
                if self._board[end_row + 2][end_col] == ally:
                    self._board[end_row + 1][end_col] = "."
                    counter += 1
        except IndexError:
            pass

        # Check left
        try:
            if self._board[end_row][end_col - 1] == enemy:
                if self._board[end_row][end_col - 2] == ally:
                    self._board[end_row][end_col - 1] = "."
                    counter += 1
        except IndexError:
            pass

        # Check right
        try:
            if self._board[end_row][end_col + 1] == enemy:
                if self._board[end_row][end_col + 2] == ally:
                    self._board[end_row][end_col + 1] = "."
                    counter += 1
        except IndexError:
            pass

        # Check top left corner
        if end_row == 1 and end_col == 2:
            if self._board[1][1] == enemy:
                if self._board[2][1] == ally:
                    self._board[1][1] = "."
                    counter += 1
        if end_row == 2 and end_col == 1:
            if self._board[1][1] == enemy:
                if self._board[1][2] == ally:
                    self._board[1][1] = "."
                    counter += 1

        # Check top right corner
        if end_row == 1 and end_col == 8:
            if self._board[1][9] == enemy:
                if self._board[2][9] == ally:
                    self._board[1][9] = "."
                    counter += 1
        if end_row == 2 and end_col == 9:
            if self._board[1][9] == enemy:
                if self._board[1][8] == ally:
                    self._board[1][9] = "."
                    counter += 1

        # Check bottom left
        if end_row == 9 and end_col == 2:
            if self._board[9][1] == enemy:
                if self._board[8][1] == ally:
                    self._board[9][1] = "."
                    counter += 1
        if end_row == 8 and end_col == 1:
            if self._board[9][1] == enemy:
                if self._board[9][2] == ally:
                    self._board[9][1] = "."
                    counter += 1

        # Check bottom right
        if end_row == 9 and end_col == 8:
            if self._board[9][9] == enemy:
                if self._board[8][9] == ally:
                    self._board[9][9] = "."
                    counter += 1
        if end_row == 8 and end_col == 9:
            if self._board[9][9] == enemy:
                if self._board[9][8] == ally:
                    self._board[9][9] = "."
                    counter += 1

        # Update pieces captured
        while counter > 0:
            if self._active_player == "BLACK":
                self._red_captured += 1
            if self._active_player == "RED":
                self._black_captured += 1
            counter -= 1

    def check_win(self):
        """Checks pieces captured and updates the game state."""
        if self._black_captured >= 9:
            self._game_state = "RED_WON"
        elif self._red_captured >= 9:
            self._game_state = "BLACK_WON"

    def make_move(self, start, end):
        """Method to make a move and update the game state to reflect it."""
        # Check the game state.
        if self._game_state != "UNFINISHED":
            print("This game has already ended.")
            return False

        # Convert the start and end points to board coordinates.
        key = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
        start_row = start[0].upper()
        start_row = key[start_row]
        start_col = int(start[1])
        end_row = end[0].upper()
        end_row = key[end_row]
        end_col = int(end[1])

        # Check if the start point has a piece to move.
        start_occupant = self.get_square_occupant(start)
        if start_occupant == "NONE":
            print("There is no piece to move.")
            return False

        # Check if its the correct player's turn.
        if start_occupant == "BLACK" and self._active_player != "BLACK":
            print("It is not your turn!")
            return False
        if start_occupant == "RED" and self._active_player != "RED":
            print("It is not your turn!")
            return False

        # Check if the move is legal and possible before making the move.
        if not self.check_move(start_row, start_col, end_row, end_col):
            print("This is not a legal move.")
            return False

        # Make the move on the game board.
        self._board[start_row][start_col] = "."
        if self._active_player == "BLACK":
            self._board[end_row][end_col] = "B"
        if self._active_player == "RED":
            self._board[end_row][end_col] = "R"

        # Make any captures caused by the move.
        self.make_capture(end_row, end_col)

        # Update game state.
        if self._active_player == "BLACK":
            self._active_player = "RED"
        elif self._active_player == "RED":
            self._active_player = "BLACK"
        self.check_win()
        if self._game_state == "BLACK_WON":
            print("Game over! Black has won.")
        elif self._game_state == "RED_WON":
            print("Game over! Red has won.")
        return True
