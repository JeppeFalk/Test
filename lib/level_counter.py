from PyQt5.QtWidgets import QLabel

class LevelCounter(QLabel):
    def __init__(self, initial_clicker_level=0, initial_passive_level=0):
        super().__init__()
        self.clicker_level = initial_clicker_level
        self.passive_clicker_level = initial_passive_level
        self.update_text()
        
    def clicker_level_increment(self, amount):
            self.clicker_level += amount
            self.update_text()

    def passive_clicker_level_increment(self, amount):
            self.passive_clicker_level += amount
            self.update_text()
    
    def update_text(self):
        self.setText(f"Clicker Level: {self.clicker_level}\nPassive Clicker Level: {self.passive_clicker_level}")