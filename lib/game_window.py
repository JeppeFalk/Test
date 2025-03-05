from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from lib.counter import Counter
from lib.level_counter import LevelCounter
from lib.button import GameButton
from lib.utils import save_game, load_game

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Clicker Game")
        self.setFixedSize(600, 400)

        # Load saved data
        data = load_game()

        # Counter
        self.counter = Counter(data['score'])
        self.counter.setParent(self)
        self.counter.move(20, -150)
        
        # Clicker Level counter
        self.level_counter = LevelCounter(data['clicker_level'])
        self.level_counter.setParent(self)
        self.level_counter.move(400, -140)
        
        # Passive Clicker Level counter
        self.passive_level_counter = LevelCounter(data['passive_clicker_level'])
        self.level_counter.setParent(self)
        self.level_counter.move(400, -130)
        
        # Click Button
        self.click_value = data['click_value']
        self.click_button = GameButton(
            text="Click Me!", x=250, y=100, width=120, height=120,
            font_size=16, on_click=self.handle_click
        )
        self.click_button.setParent(self)

        # Upgrade Button
        self.upgrade_cost = data['upgrade_cost']
        self.upgrade_button = GameButton(
            text=f"Upgrade (+1 click) - Cost: {self.upgrade_cost}",
            x=20, y=240, width=500, height=50,
            font_size=14, on_click=self.buy_upgrade
        )
        self.upgrade_button.setParent(self)
        
        # Passive Clicker Button
        self.passive_upgrade_cost = data['passive_upgrade_cost']
        self.passive_income = data['passive_income']
        self.passive_upgrade_button = GameButton(
            text=f"Upgrade (+1 passive clicker) - Cost: {self.passive_upgrade_cost}",
            x=20, y=295, width=500, height=50,
            font_size=14, on_click=self.buy_passive_clicker
        )
        self.passive_upgrade_button.setParent(self)

        # Passive Clicker Timer
        self.timer_speed = data['timer_speed']
        self.timer = QTimer()
        self.timer.timeout.connect(self.passive_gain)
        self.timer.start(self.timer_speed)  # Trigger every second
        
        # Timer speed upgrade button
        self.timer_upgrade_cost = data['timer_upgrade_cost']
        self.timer_upgrade_button = GameButton(
            text=f"Upgrade (passive clicker speed) - Cost: {self.timer_upgrade_cost}",
            x=20, y=350, width=500, height=50,
            font_size=14, on_click=self.upgrade_timer
        )
        self.timer_upgrade_button.setParent(self)
        
        # Reset button
        self.reset_button = GameButton(
            text="Reset game", x=20, y=5, width=200, height=50, font_size=14, on_click=self.reset
        )
        self.reset_button.setParent(self)

    # Add manual click value to points
    def handle_click(self):
        self.counter.increment(self.click_value)

    # Manual click upgrade
    def buy_upgrade(self):
        if self.counter.score >= self.upgrade_cost:
            self.counter.increment(-self.upgrade_cost)
            self.click_value += 1
            self.upgrade_cost *= 2
            self.upgrade_button.setText(f"Upgrade (+1 click) - Cost: {self.upgrade_cost}")
            self.level_counter.clicker_level += 1
            self.level_counter.setText(f"Clicker Level: {self.level_counter.clicker_level}")
    
    # Passive click upgrade
    def buy_passive_clicker(self):
        if self.counter.score >= self.passive_upgrade_cost:
            self.counter.increment(-self.passive_upgrade_cost)
            self.passive_income += 1
            self.passive_upgrade_cost *= 2
            self.passive_upgrade_button.setText(f"Upgrade (+1 passive clicker) - Cost: {self.passive_upgrade_cost}")
            self.level_counter.passive_clicker_level += 1

    def passive_gain(self):
        self.counter.increment(self.passive_income)
    
    # Passive click speed upgrade    
    def upgrade_timer(self):
        if self.counter.score >= self.timer_upgrade_cost and self.timer_speed > 1:
            self.counter.increment(-self.timer_upgrade_cost)
            self.timer_speed //= 2
            self.timer.start(self.timer_speed)
            self.timer_upgrade_cost *= 2
            self.timer_upgrade_button.setText(f"Upgrade (passive clicker speed) - Cost: {self.timer_upgrade_cost}")
    
    
    # Reset game        
    def reset(self):
        self.counter.score = 0
        self.level_counter.clicker_level = 1
        self.level_counter.passive_clicker_level = 0
        self.click_value = 1
        self.upgrade_cost = 10
        self.passive_upgrade_cost = 20
        self.passive_income = 0
        self.timer_speed = 1000
        self.timer.start(self.timer_speed)
        self.timer_upgrade_cost = 100
        self.level_counter.setText(f"Clicker Level: {self.level_counter.clicker_level}")
        self.upgrade_button.setText(f"Upgrade (+1 click) - Cost: {self.upgrade_cost}")
        self.passive_upgrade_button.setText(f"Upgrade (+1 passive clicker) - Cost: {self.passive_upgrade_cost}")
        self.timer_upgrade_button.setText(f"Upgrade (passive clicker speed) - Cost: {self.timer_upgrade_cost}")
        

    def closeEvent(self, event):
        save_game(self.counter.score,
                  self.level_counter.clicker_level, 
                  self.level_counter.passive_clicker_level,
                  self.click_value, 
                  self.upgrade_cost, 
                  self.passive_upgrade_cost, 
                  self.passive_income, 
                  self.timer_speed, 
                  self.timer_upgrade_cost
        )
        event.accept()
