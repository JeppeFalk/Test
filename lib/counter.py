from PyQt5.QtWidgets import QLabel

class Counter(QLabel):
    def __init__(self, initial_score=0):
        super().__init__(f"Score: {initial_score}")
        self.score = initial_score

    def increment(self, amount):
        self.score += amount
        self.setText(f"Score: {self.score}")