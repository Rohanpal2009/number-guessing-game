import random 
import time
def number_guessing_game():
    print("Hello there! I'm GuessBot, your friendly number-guessing companion.")
    time.sleep(1)
    print("I'm thinking of a secret number beteeen 1 to 100...")
    time.sleep(1)
    print("can you guess it? Let's find out!")

    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nyour guess"))
            attempts += 1

            if guess < 1 or guess >100:
                print("Hey! That's outside 1-100. Tru again")
                continue

            if guess < secret_number:
                print("Ooh... too low. aim higher!")
            elif guess >secret_number:
                print("yikes too high. Go lower!")

            else:
                print(f" Woohoo! You nailed it in {attempts} attempts!")
                if attempts <= 3:
                    print(" That's lightning fast! Are you secretly psychic?")
                elif attempts <= 7:
                    print(" Solid work! You've got great guessing skills.")
                else:
                    print(" Took a while, but you got there in the end!")
                break

        except ValueError:
            print(" That doesn't look like a number. Try typing digits only.")

    # Replay option
    play_again = input("\nWanna play again? (y/n): ").lower()
    if play_again == "y":
        number_guessing_game()
    else:
        print(" Alright, see you next time! Thanks for playing.")

if __name__ == "__main__":
    number_guessing_game()

