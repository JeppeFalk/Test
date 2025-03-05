from PyQt5.QtWidgets import QLabel

class LevelCounter(QLabel):
    def __init__(self, initial_level=0):
        super().__init__(f"Clicker Level: {initial_level}", f"Passive Clicker Level: {initial_level}")
        self.clicker_level = initial_level
        self.passive_clicker_level = initial_level
        
    def clicker_level_increment(self, amount):
            self.clicker_level += amount
            self.setText(f"Clicker Level: {self.clicker_level}")

    def passive_clicker_level_increment(self, amount):
            self.passive_clicker_level += amount
            self.setText(f"Passive Clicker Level: {self.passive_clicker_level}")