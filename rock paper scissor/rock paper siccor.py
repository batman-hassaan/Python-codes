import random

player_score = 0  
computer_score = 0 

def computer_input():
    lists = ["rock" ,"paper" ,"scissor"]

    return random.choice(lists)

def user_input():
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        choice = input("Enter your choice (rock, paper, or scissor): ").lower()
        if choice in ["rock", "paper", "scissor"]:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissor.")

def decision( player,computer):
    if player == computer :
        return "Its a tie!. "
    if (
        (player == "rock" and computer == "scissor") or
        (player == "paper" and computer == "rock") or
        (player == "scissor" and computer == "paper")
    ):
        return "you win!"
    else :
        return "you loses!"
    
def main():
    global player_score , computer_score 

    print("=" * 40)
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("=" * 40)

    while True:

        computers = computer_input()
        players = user_input()
        print(f"\n🖥️  Computer chose: {computers.capitalize()}")
        print(f"🧍 Player chose: {players.capitalize()}")

        result = decision(players,computers)
        print(result)
        if "win" in result:
                player_score += 1
        elif "lose" in result:
                computer_score += 1

        print("\n📊 Scoreboard:")
        print(f"Player: {player_score} | Computer: {computer_score}")
        print("=" * 40)

        x = input("Do you want to play again (Yes/No).").lower()
        if x == "yes":
            continue
        else :
            print("\n👋 Thanks for playing! Final scores:")
            print(f"Player: {player_score} | Computer: {computer_score}")
            print("=" * 40)
            break
main()

        # if player == decision:
        #     print(f"both chooses {decision}")
        #     print("its a tie!")
        #     break
        # if player == "rock":
        #     if decision == "paper": 
        #         print("you loses!")
        #         break
        #     elif decision == "scissor": 
        #         print("you win!")
        #         break
       
        # if player == "paper":
        #     if decision == "rock": 
        #         print("you win!")
        #         break
        #     elif decision == "scissor": 
        #         print("you lose!")
        #         break
        # if player == "scissor":
        #     if decision == "paper": 
        #         print("you win!")
        #         break
        #     elif decision == "rock": 
        #         print("you lose!")
        #         break
 