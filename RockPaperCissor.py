import random

def play_round(user_choice, bot_choice):
    """Plays a single round of Rock-Paper-Scissors."""
    if user_choice == bot_choice:
        return "It's a tie!", 0, 0  # Tie: No score change

    win_conditions = {  # Use a dictionary for cleaner win conditions
        "p": "r",  # Paper beats Rock
        "c": "p",  # Scissors beats Paper
        "r": "c",  # Rock beats Scissors
    }

    if win_conditions.get(user_choice) == bot_choice:  # Check if user wins
        return "You win!", 1, 0  # User wins: +1 user score
    else:
        return "Bot wins!", 0, 1  # Bot wins: +1 bot score


def main():
    print("Welcome to Rock-Paper-Scissors!")

    user_score = 0
    bot_score = 0
    list = ["r", "p", "c"]

    while True:
        user_choice = input("Enter r/p/c (or q to quit): ").lower()

        if user_choice == "q":
            break

        if user_choice not in list: 
            print("Invalid choice. Please enter r, p, or c.")
            continue

        bot_choice = random.choice(list)  
        print(f"Bot chose: {bot_choice}")

        result_message, user_score_change, bot_score_change = play_round(user_choice, bot_choice)
        print(result_message)

        user_score += user_score_change
        bot_score += bot_score_change

    print(f"\nFinal Score: You {user_score} - Bot {bot_score}")
    print("Thanks for playing!")


if __name__ == "__main__":  
    main()










    
