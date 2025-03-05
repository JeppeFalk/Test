from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize

class GameButton(QPushButton):
    def __init__(self, text, x, y, width=100, height=50, font_size=14, on_click=None):
        super().__init__(text)

        # Set size and position
        self.setFixedSize(QSize(width, height))
        self.move(x, y)

        # Set font
        self.setFont(QFont("Arial", font_size))

        # Default style
        self.setStyleSheet("background-color: lightblue; border-radius: 5px;")

        # Optional: connect click handler if provided
        if on_click:
            self.clicked.connect(on_click)
