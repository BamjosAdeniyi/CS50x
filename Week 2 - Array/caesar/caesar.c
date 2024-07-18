// This program performs Ceaser cyher
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool digits_only(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    // Also make sure that every character in argv[1] is a digit
    if (argc != 2 || !digits_only(argv[1]))
    {
        printf("Usage: ./ceaser key\n");
        return 1;
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("Plaintext: ");

    // For each character in the plaintext:
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        // Rotate the character if it's a letter
        plaintext[i] = rotate(plaintext[i], key);
    }

    // Prints the ciphertext
    printf("ciphertext: %s\n", plaintext);
}

// Function to check if the command line argument is only digit
bool digits_only(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

// Function to rotate the
char rotate(char c, int n)
{
    if (isalpha(c))
    {
        if (isupper(c))
        {
            c = ((int) c - 'A' + n) % 26 + 'A';
        }
        else
        {
            c = ((int) c - 'a' + n) % 26 + 'a';
        }
    }
    return c;
}