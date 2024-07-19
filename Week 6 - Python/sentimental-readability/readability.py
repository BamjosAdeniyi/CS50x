from cs50 import get_string
import re
import math


def count_letters(text):
    """Counts and returns the number of letters in a string."""
    return sum(c.isalpha() for c in text)


def count_words(text):
    """Counts and returns the number of words in a string."""
    return len(text.split())


def count_sentences(text):
    """Counts and returns the number of sentences in a string."""
    return len(re.findall(r'[.!?]', text))


def calculate_index(avg_letters, avg_sentences):
    """Calculates the approximate grade level needed to comprehend some text according to the Coleman-Liau formula."""
    return round(0.0588 * avg_letters - 0.296 * avg_sentences - 15.8)


def main():
    # Prompt the user for some text
    text = get_string("Enter the Text: ")

    # Count the number of letters, words, and sentences
    letterlen = count_letters(text)
    wordlen = count_words(text)
    sentencelen = count_sentences(text)

    # Avoid division by zero if there are no words
    if wordlen == 0:
        avg_letters = 0
        avg_sentences = 0
    else:
        avg_letters = (100 / wordlen) * letterlen
        avg_sentences = (100 / wordlen) * sentencelen

    # Compute the Coleman-Liau index
    index = calculate_index(avg_letters, avg_sentences)

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


main()
