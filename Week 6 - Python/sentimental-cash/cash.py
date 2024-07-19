def calculate_coin_num(cents):
    """Calculate the number of coins needed for a given amount of cents."""
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1

    coin_num = 0

    coin_num += cents // quarters
    cents %= quarters

    coin_num += cents // dimes
    cents %= dimes

    coin_num += cents // nickels
    cents %= nickels

    coin_num += cents // pennies
    cents %= pennies

    print(coin_num)


def main():
    owed_cents = 0
    # Prompt user for the owed amount and check that the value is valid
    while owed_cents <= 0:
        try:
            owed_amount = float(input("Change owed: "))
            if owed_amount <= 0:
                print("Amount must be greater than 0.")
                continue
            owed_cents = round(owed_amount * 100)  # Convert dollars to cents
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Print the number of coins
    calculate_coin_num(owed_cents)


main()

