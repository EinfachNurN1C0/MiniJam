import threading
import time
import random

# Global variables
energy_cans = 0
visitors = 1
visitor_price = 1  # Price increases * 2 per visitor bought
xp = 0
prestige = 0
lock = threading.Lock()  # Lock to protect global variables

def main():
    # Thread for can production
    can_timer = threading.Thread(name="can_output_proc", target=can_output, daemon=True)
    can_timer.start()

    # Menu runs in the main thread for direct user interaction
    menu()

def menu():
    global visitors, visitor_price, energy_cans

    while True:
        print(f"\n--- Choose an Option:\n< 1 > Buy Visitors - {visitors}\n< 2 > Show Cans\n< 3 > Quit")
        response = input("> ")

        if response == "1":
            print("How many visitors do you want to buy?")
            try:
                num_visitors = int(input("> "))
            except ValueError:
                print("Invalid input!")
                continue

            cost = visitor_price * (num_visitors * 2)
            
            # Critical section protected by lock
            with lock:
                if energy_cans >= cost:
                    visitors += num_visitors
                    visitor_price += num_visitors * 2
                    energy_cans -= cost
                    print(f"You've bought {num_visitors} visitors. Remaining cans: {energy_cans}")
                else:
                    print("Not enough cans!")

        elif response == "2":
            with lock:
                print(f"You have {energy_cans} cans.")

        elif response == "3":
            print("Game is quitting.")
            break

        else:
            print("Invalid input!")

def can_output():
    global energy_cans

    while True:
        can_value = random.randint(1, 10)
        earned_cans = can_value * visitors
        
        with lock:
            energy_cans += earned_cans

        # print(f"+{earned_cans} cans collected! Total: {energy_cans}")  # Debugging
        time.sleep(1)

if __name__ == "__main__":
    main()
