// This program represents the Greedy algorithm
#include <cs50.h>
#include <stdio.h>

void calculate_coin_num(int cents);

int main(void)
{
    int owed_cents = 0;
    // Prompt user for the owed coin and check that the value is valid
    while (owed_cents < 1)
    {
        owed_cents = get_int("Change owed: ");
    }
    // Print the number of coin
    calculate_coin_num(owed_cents);
}

// Function to calculate the number of coin
void calculate_coin_num(int cents)
{
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;
    int pennies = 1;

    int coin_num = 0, remain;

    coin_num += cents / quarters;
    cents %= quarters;

    coin_num += cents / dimes;
    cents %= dimes;

    coin_num += cents / nickels;
    cents %= nickels;

    coin_num += cents / pennies;
    cents %= pennies;

    printf("Coin: %i\n", coin_num);
}
