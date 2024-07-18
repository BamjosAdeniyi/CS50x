// This program create a right-aligned "#" pyramid
#include <cs50.h>
#include <stdio.h>

// Here are the function prototypes
void print_space(int height, int row);
void print_hash(int i);

int main(void)
{
    int height = 0;
    // To make sure  the user's input is valid
    while (height < 1)
    {
        height = get_int("Height: ");
    }
    // Prompt the user for the height
    for (int i = 1; i <= height; i++)
    {
        print_space(height, i);
        print_hash(i);
        printf("\n");
    }
}

// Funtion to print the spaces
void print_space(int height, int row)
{
    for (int j = 0; j < height - row; j++)
    {
        printf(" ");
    }
}

// Function to print the hash (#)
void print_hash(int i)
{
    for (int k = 0; k < i; k++)
    {
        printf("#");
    }
}
