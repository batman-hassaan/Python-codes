import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Quiz questions in format: [question, optionA, optionB, optionC, optionD, correct_option]
questions = [
    ["How many players are in a cricket team?", "11", "12", "14", "10", 1],
    ["Who is the most famous footballer on Instagram?", "Ronaldo", "Messi", "Neymar", "Ramos", 1],
    ["The fastest bike in the world is?", "H2", "ZX", "BMW", "H2R", 4],
    ["Who is the current WWE champion?", "Brock", "John Cena", "Roman", "Seth", 3],
    ["Who is the strongest character in anime?", "Saitama", "Naruto", "Goku", "Satoru", 3],
    ["Which continent is Pakistan in?", "Europe", "Asia", "Australia", "USA", 2],
    ["What is the capital of France?", "Karachi", "Madrid", "Paris", "London", 3],
    ["Who wrote 'To Kill a Mockingbird'?", "Charles Dickens", "Stephen King", "J.K. Rowling", "Harper Lee", 4],
    ["What is the chemical symbol for gold?", "Fe", "Ag", "Au", "Cu", 3],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["What is the tallest mammal?", "Kangaroo", "Elephant", "Horse", "Giraffe", 4],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo", 1]
]

# Prize money levels
levels = [1000, 5000, 10000, 20000, 25000, 50000, 100000, 150000, 220000, 360000, 500000, 1000000]

# Safe checkpoints
safe_checkpoints = {4: 20000, 7: 100000}

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome screen
def welcome():
    clear()
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "           🧠 WELCOME TO THE QUIZ GAME 🎉")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    time.sleep(2)

# Main game logic
def play_game():
    total_money = 0
    guaranteed_money = 0

    for i, q in enumerate(questions):
        clear()
        print(Fore.MAGENTA + f"Question for ₹{levels[i]}:\n")
        print(Fore.CYAN + q[0])
        print(f"a. {q[1]}       b. {q[2]}")
        print(f"c. {q[3]}       d. {q[4]}\n")
        
        ans = input(Fore.GREEN + "Enter your answer (a/b/c/d) or 'q' to quit: ").lower()

        if ans == 'q':
            print(Fore.YELLOW + f"\n🏁 You quit the game. You won ₹{total_money}")
            break

        if ans not in ['a', 'b', 'c', 'd']:
            print(Fore.RED + "Invalid option! Try again.")
            time.sleep(1)
            continue

        selected = {'a':1, 'b':2, 'c':3, 'd':4}[ans]

        if selected == q[5]:
            print(Fore.GREEN + Style.BRIGHT + "\n🎉 Correct Answer!")
            total_money += levels[i]
            if i in safe_checkpoints:
                guaranteed_money = safe_checkpoints[i]
            print(Fore.YELLOW + f"🏆 Total Money: ₹{total_money}")
        else:
            print(Fore.RED + Style.BRIGHT + "\n❌ Wrong Answer!")
            print(Fore.YELLOW + f"You go home with ₹{guaranteed_money}")
            break
        time.sleep(2)

    else:
        print(Fore.GREEN + Style.BRIGHT + "\n🏁 Congratulations! You've completed the quiz!")
        print(Fore.YELLOW + f"🎉 Total Money Won: ₹{total_money}")

# Run
welcome()
play_game()
