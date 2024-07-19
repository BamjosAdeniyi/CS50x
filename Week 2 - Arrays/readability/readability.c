// This program is for readability calculation
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Enter the Text: ");

    // Count the number of words, letters, and sentences
    int letterlen = count_letters(text);
    int wordlen = count_words(text);
    int sentencelen = count_sentences(text);

    // printf("letterlen: %i\n", letterlen);
    // printf("wordlen: %i\n", wordlen);
    // printf("sentencelen: %i\n", sentencelen);

    // Compute the Coleman-Liau index
    float avgletter = ((float) letterlen / (float) wordlen) * 100;
    float avgsentence = ((float) sentencelen / (float) wordlen) * 100;

    int index = round(0.0588 * avgletter - 0.296 * avgsentence - 15.8);

    // Print the grade level
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

// Function to count the number words in the text
int count_letters(string text)
{
    int letternum = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            letternum++;
        }
    }
    return letternum;
}

// Function to count the number letters in the text
int count_words(string text)
{
    int wordnum = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if ((text[i] != ' ' && text[i + 1] == ' '))
        {
            wordnum++;
        }
    }
    return wordnum + 1;
}

// Function to count the number sentences in the text
int count_sentences(string text)
{
    int sentencenum = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentencenum++;
        }
    }
    return sentencenum;
}
