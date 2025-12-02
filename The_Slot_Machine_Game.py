#python slot machine
import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_row(row):
    print(" ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0




def main():
    balance = 100
    is_running = True

    print("*************************")

    print("Welcome to PYTHON SLOTS")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("*************************")

    while balance > 0 and is_running :
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lose this round")

        balance += payout
        while is_running:
            play_again = input("Play again? (y/n): ").lower()

            if play_again.isdigit():
                print("Invalid input!")
                continue

            if play_again == "y" or play_again == "yes":
                print("You are welcome once again")
                break
            if play_again == "n" or play_again == "no":
                is_running = False

            else:
                print("Invalid input!")
                continue



    print(f"Thank you for playing!Your final balance is {balance}")


if __name__ == "__main__":
    main()
