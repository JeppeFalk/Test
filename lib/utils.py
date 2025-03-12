import json
import os

# Format numbers so you can read it
def format_number(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


#Save and load Game Data
SAVE_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'save.json')

def save_game(score,
              clicker_level, 
              passive_clicker_level, 
              click_value, upgrade_cost, 
              passive_upgrade_cost, 
              passive_income, timer_speed, 
              timer_upgrade_cost
              ):

    # Make sure the data folder exists
    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
    data = {
        "score": score,
        "clicker_level": clicker_level,
        "passive_clicker_level": passive_clicker_level,
        "click_value": click_value,
        "upgrade_cost": upgrade_cost,
        "passive_upgrade_cost": passive_upgrade_cost,
        "passive_income": passive_income,
        "timer_speed": timer_speed,
        "timer_upgrade_cost": timer_upgrade_cost
    }
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            return json.load(file)
    return {
        "score": 0,
        "clicker_level": 1,
        "passive_clicker_level": 0,
        "click_value": 1,
        "upgrade_cost": 10,
        "passive_upgrade_cost": 20,
        "passive_income": 0,
        "timer_speed": 1000,
        "timer_upgrade_cost": 100
    }

#Simple DEBUG print function
def log(message):
    print(f"[DEBUG] {message}")
