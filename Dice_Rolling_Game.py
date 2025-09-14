import random
loops = 0

def roll_dice():
    global loops
    while True:
        choice = input("Roll the dice? (y/n): ").strip().lower()
        if choice == "y":
            number = input("How many?: ").strip().lower()
            for die in range(int(number)):
                die = random.randrange(1,7)
                print(die)
            loops += int(number)
            print(f"You rolled the dice {loops} times in total.")                
        elif choice == "n":
            print("Thanks for playing!")
            break
        else:
            print(f'"{choice}" is not a valid choice!')

if __name__ == "__main__":
    roll_dice()
    