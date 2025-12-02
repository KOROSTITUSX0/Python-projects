import random
playing = True
while playing:

    sure = input("Are you sure to play?✅✅ (y/n): ".lower())
    if sure.isdigit():
        print("Invalid  input!")
        continue


    if not (sure == "y" or   sure == "yes"  or   sure == "n" or  sure == "no" ):
        print("Invalid  input!")
        continue

    if sure == "y" or sure == "yes":
        print("You are welcome!!!✋✅")
        break


    if sure == "n" or sure == "no":
        playing = False

        print("Thanks!")
options = ("rock" , "paper", "scissors")



while playing:
    player = None
    computer = random.choice(options)

    while player not in options :
        player = input("Enter your choice (rock , paper, scissors): ")
        if player not in options:
            print("Invalid input!")
            continue
        print(f"PLayer:{player} ")
        print(f"Computer:{computer} ")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        while playing:
            play_again = input("Do you want to play again? (y/n): ").lower()

            if play_again.isdigit():
                print("Invalid input!")
                continue

            if play_again == "y" or play_again == "yes":
                print("You are welcome once again")
                break
            if play_again == "n" or play_again == "no":
                playing = False
                print("Thanks for playing")

            else:
                print("Invalid input!")
                continue

