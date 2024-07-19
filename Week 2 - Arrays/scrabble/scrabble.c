// This program is a Scabble Game
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Point of each letter of the alphabet
int POINT[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user to enter two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute scores for the two words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    // int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // Count the score
    int score = 0;

    // Identify and add scores for each character
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isalpha(word[i]))
        {
            // Convert all the character to uppercase
            char n = toupper(word[i]);

            // Compute the score for each character
            score += POINT[n - 'A'];
        }
    }
    return score;
}
