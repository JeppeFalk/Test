



"""
This program is a simple implementation of the classic game of Tic Tac Toe using PyQt5. It defines a main window (QMainWindow) and sets up a 3x3 grid of buttons. When a button is clicked, the corresponding cell in the game board is updated with the current player's mark (either 'X' or 'O'), and the game checks for a winner. If there is no winner, the turn switches to the other player. If all cells are filled without a winner, the game ends in a draw.
The program begins by importing the necessary modules: sys for exiting the application, PyQt5.QtWidgets for the GUI elements, including QApplication, QMainWindow, QPushButton, QLabel, and QMessageBox.
The TicTacToe class is defined as a subclass of QMainWindow. Its constructor initializes the game variables (board, current_player, and winner), and calls the initUI method to create the GUI elements.
The initUI method sets the size and title of the main window, creates a QLabel to display the current player's turn, and creates a 3x3 grid of QPushButton objects to represent the cells of the game board. The buttonClicked method is connected to each button's clicked signal, which passes the row and column indices to the method as arguments.
The buttonClicked method updates the game board with the current player's mark and checks for a winner. If there is no winner, the switchPlayer method is called to change the current player. This method updates the QLabel with the new player's turn.
The checkForWinner method iterates over the rows, columns, and diagonals of the game board to check for a winning combination. If a winner is found, a message box is displayed to announce the winner. If all cells are filled without a winner, a message box is displayed to announce the draw.
Finally, the program sets up the QApplication and TicTacToe objects, and calls app.exec_() to start the event loop.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize game variables
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.current_player = 'X'
        self.winner = None

        # Create the GUI
        self.setGeometry(100, 100, 300, 350)
        self.setWindowTitle('Tic Tac Toe')

        self.label = QLabel(self)
        self.label.setGeometry(20, 20, 260, 30)
        self.label.setText('Player ' + self.current_player + '\'s turn')

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton(self)
                button.setGeometry(20 + j * 80, 60 + i * 80, 80, 80)
                button.clicked.connect(lambda _, row=i, col=j: self.buttonClicked(row, col))
                row.append(button)
            self.buttons.append(row)

        self.show()

    def buttonClicked(self, row, col):
        if self.board[row][col] == '' and not self.winner:
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            self.checkForWinner()
            if not self.winner:
                self.switchPlayer()

    def switchPlayer(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.label.setText('Player ' + self.current_player + '\'s turn')

    def checkForWinner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                self.winner = self.board[i][0]

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                self.winner = self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.winner = self.board[0][2]

        # Display winner message
        if self.winner:
            QMessageBox.information(self, 'Winner', 'Player ' + self.winner + ' has won the game!')
        elif all([cell != '' for row in self.board for cell in row]):
            QMessageBox.information(self, 'Draw', 'The game has ended in a draw.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())